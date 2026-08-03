from django.conf import settings
from django.db import models


class Announcement(models.Model):

    TYPE_CHOICES = (
        ("GENERAL", "General"),
        ("CLASS", "Class"),
        ("TIPS", "Tips"),
        ("HOLIDAY", "Holiday"),
        ("SYSTEM", "System"),
    )


    TYPE_CHOICES = (
        ("GENERAL", "General"),
        ("CLASS", "Class"),
        ("TIPS", "Tips"),
        ("HOLIDAY", "Holiday"),
        ("SYSTEM", "System"),
    )

    TARGET_CHOICES = (
        ("ALL", "All Users"),
        ("PREMIUM", "Premium Users"),
        ("STUDENT", "Students"),
    )

    title = models.CharField(
        max_length=200,
    )

    message = models.TextField()

    announcement_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default="GENERAL",
    )

    target_audience = models.CharField(
        max_length=20,
        choices=TARGET_CHOICES,
        default="ALL",
    )

    is_active = models.BooleanField(
        default=True,
    )

    publish_at = models.DateTimeField()

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

        ordering = [
            "-publish_at",
        ]

    def __str__(self):

        return self.title

class Meta:
    verbose_name = "Announcement"
    verbose_name_plural = "Announcements"