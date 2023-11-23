from django.db import models

# Create your models here.


class Carousel(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    url = models.URLField()
    url_text = models.CharField(max_length=30, default="Click")
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
