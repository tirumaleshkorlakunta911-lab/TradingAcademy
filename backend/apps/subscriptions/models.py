from django.conf import settings
from django.db import models


class PremiumSubscription(models.Model):

    STATUS_CHOICES = (
        ("ACTIVE", "Active"),
        ("EXPIRED", "Expired"),
        ("CANCELLED", "Cancelled"),
    )

    PAYMENT_STATUS = (
        ("PENDING", "Pending"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="premium_subscription",
    )

    start_date = models.DateField()

    expiry_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE",
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="PENDING",
    )

    razorpay_order_id = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    razorpay_payment_id = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    razorpay_signature = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - Premium"