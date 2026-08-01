from rest_framework import serializers

from ..models import Tip


class TipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tip
        fields = (
            "id",
            "title",
            "symbol",
            "category",
            "access_type",
            "entry_price",
            "stop_loss",
            "target_1",
            "target_2",
            "target_3",
            "description",
            "status",
            "created_at",
        )