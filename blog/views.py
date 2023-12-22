from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment
from .forms import CommentForm, PostForm

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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        # Get the uploaded image
        image = form.cleaned_data.get("image")

        # Open the image using PIL
        img = Image.open(image)

        # Convert the image to RGB format if it is not already in RGB format
        if img.mode != "RGB":
            img = img.convert("RGB")

        # Create a thumbnail of the image
        img.thumbnail((512, 512))

        # Save the thumbnail image to memory using BytesIO
        thumbnail_io = BytesIO()
        img.save(thumbnail_io, format="JPEG")

        # Save the thumbnail with the appropriate file format
        thumbnail = SimpleUploadedFile(
            name=image.name,
            content=thumbnail_io.getvalue(),
            content_type="image/jpeg",
        )

        # Set the thumbnail as the image
        form.instance.image = thumbnail

        # Call the parent class's form_valid method
        return super().form_valid(form)


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
