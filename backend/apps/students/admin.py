from django.contrib import admin

from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = (
        "student_id",
        "user",
        "city",
        "state",
        "is_active",
    )

    list_filter = (
        "is_active",
        "state",
    )

    search_fields = (
        "student_id",
        "user__full_name",
        "user__email",
    )