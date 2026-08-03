from rest_framework import serializers
from ..models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "full_name",
            "email",
            "mobile_number",
            "password",
            "confirm_password",
            "accepted_risk",
            "accepted_terms",
            "accepted_privacy",
        )

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )

        if not attrs.get("accepted_risk", False):
            raise serializers.ValidationError(
                {"accepted_risk": "Risk disclaimer must be accepted."}
            )

        if not attrs.get("accepted_terms", False):
            raise serializers.ValidationError(
                {"accepted_terms": "Terms & Conditions must be accepted."}
            )

        if not attrs.get("accepted_privacy", False):
            raise serializers.ValidationError(
                {"accepted_privacy": "Privacy Policy must be accepted."}
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")

        user = User.objects.create_user(**validated_data)

        return user