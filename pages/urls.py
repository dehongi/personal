from django.urls import path

from .views import HomePageView, AboutPageView, ContactPageView, PageDetailView

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("<slug:slug>/", PageDetailView.as_view(), name="page_detail"),
]
