from django.contrib import admin

from .models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "announcement_type",
        "target_audience",
        "publish_at",
        "is_active",
    )

    list_filter = (
        "announcement_type",
        "target_audience",
        "is_active",
    )

    search_fields = (
        "title",
    )

    ordering = (
        "-publish_at",
    )