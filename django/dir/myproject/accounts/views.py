from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 登録後にログイン
            return redirect("login")  # タスクリストへリダイレクト
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})
