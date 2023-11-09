from django.shortcuts import render

from django.views.generic import ListView

from .models import FAQ

# Create your views here.


class FAQListView(ListView):
    model = FAQ
    paginate_by = 10
    context_object_name = "faqs"
