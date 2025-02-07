from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Account

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 登録後にログイン
            return redirect("post_list")  # タスクリストへリダイレクト
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})

@login_required
def profile_edit(request):
    # ユーザーのAccountを取得、なければ作成
    account, created = Account.objects.get_or_create(user_id=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # プロフィールページにリダイレクト
    else:
        form = ProfileForm(instance=account)
    
    return render(request, 'profile_edit.html', {'form': form})
