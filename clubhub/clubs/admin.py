from django.contrib import admin
from .models import Genre, Club, Membership, Review, Feedback

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "media_type")
    list_filter = ("media_type",)

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ("name", "media_type", "genre", "description", "members")
        }),
        ("Sample 1", {
            "fields": (
                "sample_title_1",
                "sample_author_director_1",
                "sample_description_1",
                "sample_image_1",
                "sample_link_1",
            ),
            "description": "Details for the first sample book/movie."
        }),
        ("Sample 2", {
            "fields": (
                "sample_title_2",
                "sample_author_director_2",
                "sample_description_2",
                "sample_image_2",
                "sample_link_2",
            ),
            "description": "Details for the second sample book/movie."
        }),
    )

    list_display = ("name", "media_type", "genre")
    list_filter = ("media_type", "genre")
    search_fields = ("name", "description")


