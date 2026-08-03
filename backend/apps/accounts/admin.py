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
        "premium_badge",
        "active_badge",
        "created_at",
    )

    list_filter = (
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

    ordering = ("-created_at",)

    readonly_fields = (
        "created_at",
        "updated_at",
        "last_login",
    )

    fieldsets = (
        (
            "Account",
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal Information",
            {
                "fields": (
                    "full_name",
                    "mobile_number",
                )
            },
        ),
        (
            "Academy",
            {
                "fields": (
                    "user_type",
                    "is_premium",
                )
            },
        ),
        (
            "Agreements",
            {
                "fields": (
                    "accepted_risk",
                    "accepted_terms",
                    "accepted_privacy",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "last_login",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "full_name",
                    "mobile_number",
                    "password1",
                    "password2",
                    "user_type",
                    "accepted_risk",
                    "accepted_terms",
                    "accepted_privacy",
                    "is_active",
                ),
            },
        ),
    )

    actions = (
        "activate_users",
        "deactivate_users",
        "make_premium",
        "remove_premium",
    )

    @admin.display(description="Premium")
    def premium_badge(self, obj):
        return "✅" if obj.is_premium else "❌"

    @admin.display(description="Active")
    def active_badge(self, obj):
        return "🟢" if obj.is_active else "🔴"

    @admin.action(description="Activate selected users")
    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Deactivate selected users")
    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    @admin.action(description="Make Premium")
    def make_premium(self, request, queryset):
        queryset.update(is_premium=True)

    @admin.action(description="Remove Premium")
    def remove_premium(self, request, queryset):
        queryset.update(is_premium=False)\

class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"