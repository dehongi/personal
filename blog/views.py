from typing import Any
from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        form = CommentForm(initial={"post": post.id})
        context["form"] = form
        comments = self.get_object().comments.filter(active=True)
        context["comments"] = comments
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self) -> str:
        post_id = self.kwargs.get("post_id")
        post = Post.objects.get(id=post_id)
        return post.get_absolute_url()
