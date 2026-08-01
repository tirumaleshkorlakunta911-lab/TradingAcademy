from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "full_name",
        "mobile_number",
        "user_type",
        "is_premium",
        "is_active",
        "created_at",
    )

    search_fields = (
        "email",
        "full_name",
        "mobile_number",
    )

    list_filter = (
        "user_type",
        "is_premium",
        "is_active",
        "is_staff",
    )

    ordering = ("email",)