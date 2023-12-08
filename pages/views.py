from typing import Any
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, CreateView

from django.conf import settings

from .models import Carousel, Feature, Page, Message

from .forms import MessageForm

from blog.models import Post

# Create your views here.


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carousels = Carousel.objects.all()
        context["carousels"] = carousels

        features = Feature.objects.all()
        context["features"] = features

        pages = Page.objects.all()
        context["pages"] = pages

        posts = Post.objects.all()[:5]
        context["posts"] = posts

        context["site_name"] = settings.SITE_NAME
        context["site_description"] = settings.SITE_DESCRIPTION

        return context


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class ContactPageView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "pages/contact.html"

    def get_success_url(self) -> str:
        return reverse("pages:contact_success")


class ContactSuccessPage(TemplateView):
    template_name = "pages/success.html"


class PrivacyPageView(TemplateView):
    template_name = "pages/privacy.html"


class TermsOfServicePageView(TemplateView):
    template_name = "pages/terms.html"


class PageDetailView(DetailView):
    model = Page


class FeatureDetailView(DetailView):
    model = Feature
