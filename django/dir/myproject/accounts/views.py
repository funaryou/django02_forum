from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Account
from .models import User
from forum_app.models import Post
import random



def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
# ランダムなデフォルトプロフィール画像を設定
            default_image = "profile_images/default" + str(random.randint(1, 6)) + ".png"

            # Account インスタンスを作成し、User に紐づける
            account = Account.objects.create(user_id=user, profile_image=default_image)

            user.save()  # 変更を保存
            login(request, user)  # 登録後にログイン

            return redirect("post_list")  # タスクリストへリダイレクト
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})

@login_required
def profile_edit(request,pk):
    # ユーザーのAccountを取得、なければ作成
    user = User.objects.get(pk=pk)
    account, created = Account.objects.get_or_create(user_id=request.user)
    
    if request.method == 'POST':
        
        user_name = request.POST.get("user_name")
        profile_image = request.FILES.get("profile_image") 
        profile_comment = request.POST.get("profile_comment")

        user.username = user_name
        user.save()
        
        account.profile_comment = profile_comment
        
        # プロフィール画像が送信されていれば更新
        if profile_image:
            account.profile_image = profile_image
        account.save()

        return redirect(f'../detail/{user.id}')  
    return render(request, 'profile_edit.html', {'account': account,'user': user,})





@login_required
def profile_detail(request, pk):
    user = User.objects.get(pk=pk)
    profile = Account.objects.get(user_id_id=pk)
    posts = Post.objects.filter(author=user).order_by('-created_at')
    return render(request, 'profile_detail.html', {'user_profile': user, "profile": profile, 'posts': posts, 'user': request.user})
