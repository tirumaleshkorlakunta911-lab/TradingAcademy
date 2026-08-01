from rest_framework import serializers
from ..models import User


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
            "email",
            "mobile_number",
            "student_id",
            "user_type",
            "profile_image",
            "is_premium",
            "accepted_risk",
            "accepted_terms",
            "accepted_privacy",
            "created_at",
        )

        read_only_fields = (
            "id",
            "email",
            "student_id",
            "user_type",
            "is_premium",
            "created_at",
        )