from django.contrib import admin

from .models import CourseResource


@admin.register(CourseResource)
class CourseResourceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "resource_type",
        "category",
        "is_active",
        "created_at",
    )

    list_filter = (
        "resource_type",
        "category",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "-created_at",
    )