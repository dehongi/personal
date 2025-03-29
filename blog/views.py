from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

from django.views.generic import ListView, DetailView, CreateView
from taggit.models import Tag

from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.


class PostListView(ListView):
    """Display a list of published blog posts."""

    model = Post
    context_object_name = "posts"
    paginate_by = 5
    queryset = Post.published.all()
    template_name = "blog/post_list.html"


class PostListByTagView(ListView):
    """Display posts filtered by tag."""

    model = Post
    context_object_name = "posts"
    paginate_by = 5
    template_name = "blog/post_list.html"

    def get_queryset(self):
        """Filter posts by tag."""
        self.tag = get_object_or_404(Tag, slug=self.kwargs["tag_slug"])
        return Post.published.filter(tags__in=[self.tag])

    def get_context_data(self, **kwargs):
        """Add tag to context."""
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context


class PostSearchView(ListView):
    """Search for posts by title, body, or tags."""

    model = Post
    context_object_name = "posts"
    paginate_by = 5
    template_name = "blog/post_search.html"

    def get_queryset(self):
        """Filter posts by search query."""
        query = self.request.GET.get("query", "")
        if query:
            return Post.published.filter(
                Q(title__icontains=query)
                | Q(body__icontains=query)
                | Q(tags__name__icontains=query)
            ).distinct()
        return Post.published.none()

    def get_context_data(self, **kwargs):
        """Add search query to context."""
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("query", "")
        return context


class PostDetailView(DetailView):
    """Display a single blog post with comments."""

    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        """Add comment form, comments and related posts to context."""
        context = super().get_context_data(**kwargs)
        # Add comment form
        form = CommentForm()
        context["form"] = form

        # Add comments
        post = self.get_object()
        comments = post.comments.filter(active=True)
        context["comments"] = comments

        # Add related posts by tags
        post_tags_ids = post.tags.values_list("id", flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(
            id=post.id
        )
        similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
            "-same_tags", "-publish"
        )[:4]
        context["similar_posts"] = similar_posts

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """Create a new blog post."""

    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    login_url = "/admin/login/"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Process valid form, setting author and optimizing image."""
        form.instance.author = self.request.user
        # Get the uploaded image
        image = form.cleaned_data.get("image")

        if image:
            # Open the image using PIL
            img = Image.open(image)

            # Convert the image to RGB format if it is not already in RGB format
            if img.mode != "RGB":
                img = img.convert("RGB")

            # Create a thumbnail of the image
            img.thumbnail((800, 600))

            # Save the thumbnail image to memory using BytesIO
            thumbnail_io = BytesIO()
            img.save(thumbnail_io, format="JPEG", quality=85)

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
    """Create a new comment on a blog post."""

    def post(self, request, post_id):
        """Process comment form submission."""
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post.get_absolute_url())

        # If form is not valid, return to post detail with form errors
        comments = post.comments.filter(active=True)
        return render(
            request,
            "blog/post_detail.html",
            {"post": post, "form": form, "comments": comments},
        )
