from rest_framework import serializers

from .models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):

    created_by = serializers.CharField(
        source="created_by.full_name",
        read_only=True,
    )

    class Meta:

        model = Announcement

        fields = (
            "id",
            "title",
            "message",
            "announcement_type",
            "target_audience",
            "publish_at",
            "created_by",
            "created_at",
        )