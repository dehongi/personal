from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

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
        form = CommentForm()
        context["form"] = form
        comments = self.get_object().comments.filter(active=True)
        context["comments"] = comments
        return context


class CommentCreateView(View):
    def post(self, request, post_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, id=post_id)
            comment.save()
            return redirect("blog:post_detail_id", pk=post_id)
        else:
            # Handle the case where the form is not valid.
            # You could redirect back to the post detail page with an error message.
            pass
