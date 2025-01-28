from django.shortcuts import render ,redirect,get_object_or_404

# Create your views here.
#myapp/views.py
from django.http import HttpResponse



from .models import Post
from . import views
from .forms import PostForm

# from django.contrib.auth.decorators import login_required

# def index(request):
#     return render(request, 'index.html')  # テンプレートを適宜変更

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html',{'posts':posts})


def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html',{'post':post})
