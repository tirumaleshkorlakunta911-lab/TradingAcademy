from django.contrib import admin

from .models import PremiumPayment


@admin.register(PremiumPayment)
class PremiumPaymentAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "amount",
        "status",
        "created_at",
    )

    search_fields = (
        "user__email",
        "user__full_name",
    )

    list_filter = (
        "status",
    )