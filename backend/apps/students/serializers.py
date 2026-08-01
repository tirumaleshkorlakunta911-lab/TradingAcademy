from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        source="user.full_name",
        read_only=True,
    )

    email = serializers.EmailField(
        source="user.email",
        read_only=True,
    )

    class Meta:

        model = Student

        fields = (
            "student_id",
            "name",
            "email",
            "batch_name",
            "mentor_name",
            "course_start_date",
            "course_end_date",
            "status",
        )