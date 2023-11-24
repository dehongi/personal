from django.db import models

from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class Carousel(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    image = models.ImageField(upload_to="carousel")

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
    slug = models.SlugField(max_length=256, unique=True, editable=False)
    image = models.ImageField(upload_to="pages")
    intro = models.TextField()
    body = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


""" @receiver(pre_save, sender=Page)
def update_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title) """
