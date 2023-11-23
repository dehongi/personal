from django.db import models

# Create your models here.


class Carousel(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to="carousel")
