from django import forms
from .models import Page, Message


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ["title", "slug", "intro", "body", "image"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "message"]
