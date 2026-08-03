from django.db import models


class LiveClass(models.Model):

    PLATFORM_CHOICES = (
        ("ZOOM", "Zoom"),
        ("GOOGLE_MEET", "Google Meet"),
        ("MICROSOFT_TEAMS", "Microsoft Teams"),
    )

    STATUS_CHOICES = (
        ("UPCOMING", "Upcoming"),
        ("LIVE", "Live"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    trainer_name = models.CharField(
        max_length=100,
    )

    meeting_platform = models.CharField(
        max_length=30,
        choices=PLATFORM_CHOICES,
    )

    meeting_link = models.URLField()

    meeting_id = models.CharField(
        max_length=100,
        blank=True,
    )

    meeting_password = models.CharField(
        max_length=100,
        blank=True,
    )

    scheduled_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="UPCOMING",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["scheduled_date", "start_time"]

    def __str__(self):
        return self.title

class Meta:
    verbose_name = "Live Class"
    verbose_name_plural = "Live Classes"