from django.utils import timezone

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from apps.common.responses import success_response, error_response

from apps.students.models import Student
from apps.attendance.models import Attendance

from .models import LiveClass
from .serializers import LiveClassSerializer



class UpcomingClassesView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):

        classes = LiveClass.objects.filter(
            scheduled_date__gte=timezone.now().date(),
            status="UPCOMING",
        ).order_by(
            "scheduled_date",
            "start_time",
        )

        serializer = LiveClassSerializer(
            classes,
            many=True,
        )

        return success_response(
            data=serializer.data,
            message="Upcoming classes fetched successfully.",
        )

class LiveClassDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, pk):

        live_class = get_object_or_404(
            LiveClass,
            pk=pk,
        )

        serializer = LiveClassSerializer(live_class)

        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )

class JoinClassView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, pk):

        # Check active student
        student = Student.objects.get(
            user=request.user,
            status="ACTIVE",
        )

        # Fetch class
        live_class = get_object_or_404(
            LiveClass,
            pk=pk,
        )

        # Validate class status
        if live_class.status != "LIVE":
            return error_response(
                message="This class is not live.",
            )

        # Mark attendance
        Attendance.objects.get_or_create(
            student=student,
            live_class=live_class,
            defaults={
                "status": "PRESENT",
            },
        )

        return success_response(
            message="Joining class...",
            data={
                "meeting": {
                    "platform": live_class.meeting_platform,
                    "link": live_class.meeting_link,
                    "meeting_id": live_class.meeting_id,
                    "password": live_class.meeting_password,
                }
            }
        )
