from django.contrib import admin

from .models import Tip


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):

    list_display = (
        "symbol",
        "category",
        "access_type",
        "status",
        "created_at",
    )

    list_filter = (
        "category",
        "access_type",
        "status",
    )

    search_fields = (
        "symbol",
        "title",
    )

    ordering = (
        "-created_at",
    )