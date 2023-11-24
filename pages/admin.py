from django.contrib import admin

from .models import Carousel, Feature, Page

# Register your models here.

admin.site.register(Carousel)
admin.site.register(Feature)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "image", "intro", "body"]
    list_filter = [
        "title",
    ]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["title", "intro"]
