from django.contrib import admin

from .models import LiveClass


@admin.register(LiveClass)
class LiveClassAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "trainer_name",
        "scheduled_date",
        "start_time",
        "status",
    )

    list_filter = (
        "status",
        "meeting_platform",
        "scheduled_date",
    )

    search_fields = (
        "title",
        "trainer_name",
    )

    ordering = (
        "-scheduled_date",
    )