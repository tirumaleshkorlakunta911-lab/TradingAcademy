from django.contrib import admin

from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "live_class",
        "status",
        "joined_at",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "student__student_id",
        "live_class__title",
    )