from tkinter import PhotoImage
from django.shortcuts import get_object_or_404, render

from .models import Post,PostImage


def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts':posts})


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    context = {
        'post':post,
        'photos':photos
    }
    return render(request, 'posts/detail.html', context)