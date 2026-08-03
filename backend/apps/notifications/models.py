from django.conf import settings
from django.db import models

from apps.announcements.models import Announcement


class Notification(models.Model):

    TYPE_CHOICES = (
        ("GENERAL", "General"),
        ("CLASS", "Class"),
        ("TIPS", "Tips"),
        ("SYSTEM", "System"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=200,
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default="GENERAL",
    )

    is_read = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

class Meta:
    verbose_name = "Notification"
    verbose_name_plural = "Notifications"