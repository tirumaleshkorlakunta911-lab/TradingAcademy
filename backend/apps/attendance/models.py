from django.db import models

from apps.students.models import Student
from apps.classes.models import LiveClass


class Attendance(models.Model):

    STATUS_CHOICES = (
        ("PRESENT", "Present"),
        ("ABSENT", "Absent"),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="attendance",
    )

    live_class = models.ForeignKey(
        LiveClass,
        on_delete=models.CASCADE,
        related_name="attendance",
    )

    joined_at = models.DateTimeField(
        auto_now_add=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PRESENT",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = [
            "-joined_at",
        ]

        unique_together = (
            "student",
            "live_class",
        )

    def __str__(self):
        return f"{self.student.student_id} - {self.live_class.title}"