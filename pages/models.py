from django.db import models
from django.urls import reverse

from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class Carousel(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    image = models.ImageField(upload_to="carousel")
    image_mobile = models.ImageField(upload_to="carousel", blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=50)
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to="features")

    def __str__(self) -> str:
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique_for_date="created")
    image = models.ImageField(upload_to="pages")
    intro = models.TextField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    show_on_home = models.BooleanField(default=False)
    add_to_main_menu = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("pages:page_detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.subject
