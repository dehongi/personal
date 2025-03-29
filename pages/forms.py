from django import forms
from .models import Page, Message


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ["title", "slug", "intro", "body", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "intro": forms.Textarea(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }
