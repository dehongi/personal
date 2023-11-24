from django.db import models

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
    slug = models.SlugField(max_length=256, unique=True)
    image = models.ImageField(upload_to="pages")
    intro = models.TextField()
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
