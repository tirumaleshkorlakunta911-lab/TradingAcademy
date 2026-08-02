from rest_framework import serializers

from .models import Recording


class RecordingSerializer(serializers.ModelSerializer):

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

        model = Recording

        fields = (
            "id",
            "title",
            "description",
            "class_name",
            "trainer",
            "class_date",
            "video",
            "thumbnail",
            "duration",
            "is_active",
            "created_at",
        )