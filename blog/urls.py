from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    CommentCreateView,
    PostCreateView,
    PostListByTagView,
    PostSearchView,
)

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("tag/<slug:tag_slug>/", PostListByTagView.as_view(), name="post_list_by_tag"),
    path("search/", PostSearchView.as_view(), name="post_search"),
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
