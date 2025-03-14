from django.shortcuts import render ,redirect,get_object_or_404
from django.db.models import Q

# Create your views here.
#myapp/views.py
from django.http import HttpResponse



from .models import Post
from .models import Reply
from . import views
from .forms import PostForm

# from django.contrib.auth.decorators import login_required

# def index(request):
#     return render(request, 'index.html')  # テンプレートを適宜変更

from django.contrib.auth.decorators import login_required


def post_list(request):
    query = request.GET.get('q')  # 検索クエリを取得
    if query:
        # タイトルまたは内容に検索クエリが含まれる投稿を検索
        posts = Post.objects.filter(
            Q(title__icontains=query) |  # タイトルで検索
            Q(content__icontains=query) |
            Q(author__username__icontains=query) |
            Q(created_at__icontains=query) # 内容で検索
        ).order_by('-created_at')
    else:
        # 検索クエリがない場合は全ての投稿を表示
        posts = Post.objects.all().order_by('-created_at')
    
    return render(request, 'post_list.html', {'posts': posts, 'query': query})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    replys = Reply.objects.filter(post=post)  # 投稿に関連するリプライを取得
    return render(request, 'post_detail.html', {'post': post, 'replys': replys}) 

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)  # まだDBに保存しない
            new_post.author = request.user  # ログインユーザーを著者に設定
            new_post.save()  # ここで保存
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)  # `task` ではなく `post` に統一
    if request.user == post.author :
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_list')
        else:
            form = PostForm(instance=post)
        return render(request, 'post_edit.html', {'form': form})
    else :
        return redirect('post_list')


@login_required
def post_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.user == post.author :
        if request.method == 'POST':
            post.delete()
            return redirect('post_list')
        return render(request,'post_confirm_delete.html',{'post':post})
    else :
        return redirect('post_list')



@login_required
def reply_create(request, pk):
    post = get_object_or_404(Post, pk=pk)  # 投稿を取得
    if request.method == 'POST':
        content = request.POST.get('content')  # リプライの内容を取得
        parent_reply_id = request.POST.get('parent_reply_id')  # 親リプライのIDを取得
        parent_reply = Reply.objects.get(id=parent_reply_id) if parent_reply_id else None  # 親リプライがあれば取得

        # 新しいリプライを作成
        reply = Reply.objects.create(post=post, content=content, parent_reply=parent_reply)
        return redirect('post_detail', pk=post.pk)  # 投稿詳細ページにリダイレクト

    return render(request, 'reply_create.html', {'post': post})  # GETリクエストの場合は投稿詳細を表示
