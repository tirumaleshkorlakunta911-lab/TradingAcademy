from django.conf import settings
from django.db import models


class CourseResource(models.Model):

    RESOURCE_TYPE_CHOICES = (
        ("PDF", "PDF"),
        ("EXCEL", "Excel"),
        ("DOC", "Document"),
        ("PPT", "PowerPoint"),
        ("ZIP", "ZIP"),
    )

    CATEGORY_CHOICES = (
        ("BASIC", "Basic"),
        ("ADVANCED", "Advanced"),
        ("PRICE_ACTION", "Price Action"),
        ("OPTIONS", "Options"),
        ("RISK_MANAGEMENT", "Risk Management"),
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    resource_type = models.CharField(
        max_length=20,
        choices=RESOURCE_TYPE_CHOICES,
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
    )

    file = models.FileField(
        upload_to="resources/",
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
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
        return self.title