from rest_framework.response import Response
from rest_framework import viewsets, permissions
from django.db import IntegrityError
from .serializers import *


class ProfileAPIViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # to create a permission IsOwner and implement here
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, args, kwargs)
        except IntegrityError as e:
            if 'UNIQUE constraint failed: api_profile.user_id' in e.args:
                return Response({'error': 'current user already has the profile'})
            else:
                return Response({'error': e.args})


class QuestionAPIViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerAPIViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuizAPIViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Quizz.objects.all()
    serializer_class = QuizzSerializer
