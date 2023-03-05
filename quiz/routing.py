from django.urls import path
from quiz.consumers import QuizConsumer

websocket_urlpatterns = [
    path("<str:room_name>/", QuizConsumer.as_asgi()),
]