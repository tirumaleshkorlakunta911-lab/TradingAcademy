from rest_framework import serializers

from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):

    class_name = serializers.CharField(
        source="live_class.title",
        read_only=True,
    )

    trainer = serializers.CharField(
        source="live_class.trainer_name",
        read_only=True,
    )

    class_date = serializers.DateField(
        source="live_class.scheduled_date",
        read_only=True,
    )

    class Meta:
        model = Attendance

        fields = (
            "id",
            "class_name",
            "trainer",
            "class_date",
            "status",
            "joined_at",
        )