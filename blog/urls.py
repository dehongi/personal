from django.urls import path

from .views import PostListView, PostDetailView, CommentCreateView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/",
        PostDetailView.as_view(),
        name="post_detail",
    ),
    path("<int:post_id>/comment/add/", CommentCreateView.as_view(), name="comment_create"),
]
