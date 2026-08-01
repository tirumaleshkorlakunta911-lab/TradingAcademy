from django.conf import settings
from django.db import models


class Student(models.Model):

    STATUS_CHOICES = (
        ("ACTIVE", "Active"),
        ("COMPLETED", "Completed"),
        ("EXPIRED", "Expired"),
        ("SUSPENDED", "Suspended"),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student",
    )

    student_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
    )

    batch_name = models.CharField(
        max_length=100,
    )

    mentor_name = models.CharField(
        max_length=100,
    )

    course_start_date = models.DateField()

    course_end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.student_id} - {self.user.email}"

def save(self, *args, **kwargs):

    if not self.student_id:

        last_student = Student.objects.order_by("-id").first()

        if last_student:
            last_number = int(last_student.student_id.replace("TA", ""))
            self.student_id = f"TA{last_number + 1:06d}"
        else:
            self.student_id = "TA000001"

    super().save(*args, **kwargs)