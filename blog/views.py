from typing import Any
from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Post, Comment

# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        comments = (
            self.get_object().comments().filter(active=True)
        )  # only active comments
        context["comments"] = comments
        return context
