from django.contrib import admin

from .models import Carousel, Feature, Page, Message

# Register your models here.

admin.site.register(Carousel)
admin.site.register(Feature)
admin.site.register(Message)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "image", "intro", "body"]
    list_filter = [
        "title",
    ]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "body"]
    ordering = ["title", "intro"]
