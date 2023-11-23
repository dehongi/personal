from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Carousel

# Create your views here.


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carousels = Carousel.objects.all()
        context["carousels"] = carousels
        return context


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class ContactPageView(TemplateView):
    template_name = "pages/contact.html"
