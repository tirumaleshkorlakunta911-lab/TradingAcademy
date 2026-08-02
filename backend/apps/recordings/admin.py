from django.contrib import admin

from .models import Recording


@admin.register(Recording)
class RecordingAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "live_class",
        "duration",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "live_class__title",
    )

    ordering = (
        "-created_at",
    )