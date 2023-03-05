import random

from db_management.models import Question, Answer
N_QUESTIONS = 10


class DataQuestion:
    def __init__(self, answers=None, correct=None):
        self.answers = answers
        self.correct_answer = correct


def get_random_quiz(topic=True):
    data_questions = []
    for question in Question.objects.all():
        data_question = DataQuestion()
        answers = []
        for answer in Answer.objects.get(question=question):
            if answer.is_correct:
                data_question.correct_answer = answer
        data_question.answers = answers
    return random.sample(data_questions, N_QUESTIONS)
