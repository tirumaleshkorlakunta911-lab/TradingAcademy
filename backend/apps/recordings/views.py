from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.responses import success_response
from apps.students.permissions import IsStudent

from .models import Recording
from .serializers import RecordingSerializer


class RecordingListView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsStudent,
    ]

    def get(self, request):

        recordings = Recording.objects.filter(
            is_active=True,
        )

        serializer = RecordingSerializer(
            recordings,
            many=True,
        )

        return success_response(
            data=serializer.data,
            message="Recordings fetched successfully.",
        )


class RecordingDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsStudent,
    ]

    def get(self, request, pk):

        recording = get_object_or_404(
            Recording,
            pk=pk,
            is_active=True,
        )

        serializer = RecordingSerializer(recording)

        return success_response(
            data=serializer.data,
            message="Recording fetched successfully.",
        )


class RecordingByClassView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsStudent,
    ]

    def get(self, request, class_id):

        recording = get_object_or_404(
            Recording,
            live_class_id=class_id,
            is_active=True,
        )

        serializer = RecordingSerializer(recording)

        return success_response(
            data=serializer.data,
            message="Recording fetched successfully.",
        )