from django.contrib import admin

from .models import PremiumSubscription


@admin.register(PremiumSubscription)
class PremiumSubscriptionAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "status",
        "payment_status",
        "start_date",
        "expiry_date",
    )

    search_fields = (
        "user__email",
        "user__full_name",
    )

    list_filter = (
        "status",
        "payment_status",
    )