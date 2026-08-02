from rest_framework import serializers

from .models import LiveClass


class LiveClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = LiveClass

        fields = (
            "id",
            "title",
            "description",
            "trainer_name",
            "meeting_platform",
            "scheduled_date",
            "start_time",
            "end_time",
            "status",
        )