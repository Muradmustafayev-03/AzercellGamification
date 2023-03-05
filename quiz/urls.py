from django.urls import path
from quiz import views

urlpatterns = [
    path("<str:room_name>/", views.quizPage, name="quiz-page"),
]