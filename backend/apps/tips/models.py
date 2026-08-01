from django.conf import settings
from django.db import models


class Tip(models.Model):

    CATEGORY_CHOICES = (
        ("EQUITY", "Equity"),
        ("FNO", "Futures & Options"),
        ("INDEX_FNO", "Index Futures & Options"),
        ("CATEGORY_4", "Category 4"),
    )

    STATUS_CHOICES = (
        ("ACTIVE", "Active"),
        ("TARGET_1_HIT", "Target 1 Hit"),
        ("TARGET_2_HIT", "Target 2 Hit"),
        ("TARGET_3_HIT", "Target 3 Hit"),
        ("STOPLOSS_HIT", "Stop Loss Hit"),
        ("CLOSED", "Closed"),
    )

    title = models.CharField(
        max_length=200,
    )

    symbol = models.CharField(
        max_length=50,
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
    )

    ACCESS_CHOICES = (
        ("FREE", "Free"),
        ("PREMIUM", "Premium"),
    )

    access_type = models.CharField(
        max_length=20,
        choices=ACCESS_CHOICES,
        default="FREE",
    )

    entry_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    stop_loss = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    target_1 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    target_2 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    target_3 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE",
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tips",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.symbol} ({self.category})"