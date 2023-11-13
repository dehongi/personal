from django.db import models

# Create your models here.
"""_summary_

    Returns:
        _type_: _description_
        
        In the code above, we have added four new models:

ThemeScript: Represents external script files used by the theme.
ThemeFont: Represents external font files used by the theme.
ThemeMetaTag: Represents meta tags used by the theme for SEO purposes.
ThemeIntegration: Represents external integrations (e.g., Google Analytics, social media) used by the theme.
These new models provide additional flexibility and extensibility for themes in your application.
"""


class Theme(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class ThemeImage(models.Model):
    theme = models.ForeignKey("Theme", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="themes/")

    class Meta:
        verbose_name = "theme-image"
        verbose_name_plural = "theme-images"


class ThemeCSS(models.Model):
    theme = models.ForeignKey(
        "Theme", on_delete=models.CASCADE, related_name="cssfiles"
    )
    url = models.URLField()


class ThemeScript(models.Model):
    theme = models.ForeignKey(
        "Theme", on_delete=models.CASCADE, related_name="scriptfiles"
    )
    url = models.URLField()


class ThemeFont(models.Model):
    theme = models.ForeignKey("Theme", on_delete=models.CASCADE, related_name="fonts")
    url = models.URLField()


class ThemeMetaTag(models.Model):
    theme = models.ForeignKey(
        "Theme", on_delete=models.CASCADE, related_name="metatags"
    )
    name = models.CharField(max_length=100)
    content = models.TextField()


class ThemeIntegration(models.Model):
    theme = models.ForeignKey(
        "Theme", on_delete=models.CASCADE, related_name="integrations"
    )
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)
