from django.urls import path

from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    PageDetailView,
    PrivacyPageView,
    TermsOfServicePageView,
    ContactSuccessPage,
    FeatureDetailView,
)

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("contact/success/", ContactSuccessPage.as_view(), name="contact_success"),
    path("privacy/", PrivacyPageView.as_view(), name="privacy"),
    path("terms/", TermsOfServicePageView.as_view(), name="terms"),
    path("<slug:slug>/", PageDetailView.as_view(), name="page_detail"),
    path("feature/<int:pk>/", FeatureDetailView.as_view(), name="feature_detail"),
]
