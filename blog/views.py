from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
