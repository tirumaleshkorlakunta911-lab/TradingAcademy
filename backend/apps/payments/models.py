from django.conf import settings
from django.db import models


class PremiumPayment(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="premium_payments",
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    razorpay_order_id = models.CharField(
        max_length=200,
        unique=True,
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

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.user.email} - ₹{self.amount}"