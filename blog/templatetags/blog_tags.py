from django import template

from django.db.models import Count

from django.utils.safestring import mark_safe
import markdown

from ..models import Post
from taggit.models import Tag

register = template.Library()


@register.simple_tag
def total_posts():
    """Return the total number of published posts."""
    return Post.published.count()


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    """Display the latest posts in the sidebar."""
    latest_posts = Post.published.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    """Get the most commented posts."""
    return Post.published.annotate(total_comments=Count("comments")).order_by(
        "-total_comments"
    )[:count]


@register.inclusion_tag("blog/post/tags_list.html")
def get_tags_with_count():
    """Get all tags with the count of posts using them."""
    tags = Tag.objects.annotate(post_count=Count("taggit_taggeditem_items"))
    return {"tags": tags}


@register.filter(name="markdown")
def markdown_format(text):
    """Convert markdown text to HTML."""
    return mark_safe(markdown.markdown(text, extensions=["extra", "codehilite"]))
