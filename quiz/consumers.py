import json
from .models import Player
from .quiz_questions import get_random_quiz
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class QuizConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.players = []
        self.questions = get_random_quiz()

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name,
        )

    def get_player_by_username(self, username):
        for player in self.players:
            if player.user == username:
                return player
        player = Player.objects.get_or_create(user=username)
        self.players.append(player)
        return player

    async def receive(self, text_data=None, **kwargs):
        text_data_json = json.loads(text_data)
        answer = text_data_json["answer"]
        username = text_data_json["username"]

        player = await self.get_player_by_username(username)
        question = self.questions[player.questions_answered]

        if question.correct_answer == answer:
            player.answers_correct += 1

        await self.channel_layer.group_send(
            self.room_name, {
                "type": "sendMessage",
                "question": question,
                "username": player.user,
                "question_index": player.questions_answered
            })
        player.questions_answered += 1

    async def sendMessage(self, event):
        question = event["question"]
        username = event["username"]
        room_name = event["room_name"]
        question_index = event["question_index"]
        await self.send(text_data=json.dumps({
            "question": question,
            "username": username,
            "room_name": room_name,
            "question_index": question_index
        }))
