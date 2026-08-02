from django.conf import settings
from django.db import models

from apps.classes.models import LiveClass


class Recording(models.Model):

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    live_class = models.OneToOneField(
        LiveClass,
        on_delete=models.CASCADE,
        related_name="recording",
    )

    video = models.FileField(
        upload_to="recordings/videos/",
        blank=True,
        null=True,
    )

    video_size = models.PositiveBigIntegerField(
        null=True,
        blank=True,
    )

    thumbnail = models.ImageField(
        upload_to="recordings/thumbnails/",
        blank=True,
        null=True,
    )

    duration = models.CharField(
        max_length=20,
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