from django.urls import path

from .views import PostListView, PostDetailView, CommentCreateView, PostCreateView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("write/", PostCreateView.as_view(), name="write_post"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/",
        PostDetailView.as_view(),
        name="post_detail",
    ),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail_id"),
    path(
        "<int:post_id>/comment/",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
]
