from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "student_id",
        "user",
        "batch_name",
        "mentor_name",
        "status",
        "course_end_date",
    )

    search_fields = (
        "student_id",
        "user__email",
    )

    list_filter = (
        "status",
        "batch_name",
    )

class Meta:
    verbose_name = "Student"
    verbose_name_plural = "Students"