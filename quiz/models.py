from django.db import models


class Player(models.Model):
    user = models.CharField(max_length=100)
    questions_answered = models.PositiveIntegerField(default=0)
    answers_correct = models.PositiveIntegerField(default=0)
