from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register(r'profiles', ProfileAPIViewSet)
router.register(r'questions', QuestionAPIViewSet)
router.register(r'answers', AnswerAPIViewSet)
router.register(r'quizzes', QuizAPIViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
