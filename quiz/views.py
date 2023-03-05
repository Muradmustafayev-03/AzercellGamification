from django.shortcuts import render, redirect


def quizPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {'room_id': kwargs['room_name']}
    return render(request, "quizPage.html", context)
