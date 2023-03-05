from django.contrib.auth.models import User
from django.db import models

TOPICS = [
    ('Topic 1', 'Topic 1'),
    ('Topic 2', 'Topic 2'),
    ('Topic 3', 'Topic 3')
]


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)

    bonus = models.PositiveIntegerField(verbose_name='Aardvarks',
                                        default=0)

    rating = models.PositiveIntegerField(verbose_name='score points',
                                         default=0)


class Question(models.Model):
    title = models.CharField(max_length=100)
    topic = models.CharField(choices=TOPICS, max_length=100)
    # Time in seconds given to users to answer the question dependent on its difficulty
    duration = models.PositiveIntegerField(default=10)


class Answer(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_correct = models.BooleanField()


class Quizz(models.Model):
    topic = models.CharField(choices=TOPICS, max_length=100)
    questions = models.ManyToManyField(Question)
