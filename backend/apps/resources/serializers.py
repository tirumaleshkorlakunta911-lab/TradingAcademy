from rest_framework import serializers

from .models import CourseResource


class CourseResourceSerializer(serializers.ModelSerializer):

    class Meta:

        model = CourseResource

        fields = (
            "id",
            "title",
            "description",
            "resource_type",
            "category",
            "file",
            "is_active",
            "created_at",
        )