from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.responses import success_response
from apps.students.permissions import IsStudent

from .models import CourseResource
from .serializers import CourseResourceSerializer
from django.shortcuts import get_object_or_404


class ResourceListView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsStudent,
    ]

    def get(self, request):

        resources = CourseResource.objects.filter(
            is_active=True
        )

        serializer = CourseResourceSerializer(
            resources,
            many=True,
        )

        return success_response(
            data=serializer.data,
            message="Resources fetched successfully.",
        )

class ResourceDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsStudent,
    ]

    def get(self, request, pk):

        resource = get_object_or_404(
            CourseResource,
            pk=pk,
            is_active=True,
        )

        serializer = CourseResourceSerializer(resource)

        return success_response(
            data=serializer.data,
            message="Resource fetched successfully.",
        )

class ResourceCategoryView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsStudent,
    ]

    def get(self, request, category):

        resources = CourseResource.objects.filter(
            category=category,
            is_active=True,
        )

        serializer = CourseResourceSerializer(
            resources,
            many=True,
        )

        return success_response(
            data=serializer.data,
            message="Category resources fetched successfully.",
        )