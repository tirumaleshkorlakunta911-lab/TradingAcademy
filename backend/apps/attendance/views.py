from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.responses import success_response
from apps.students.models import Student

from .models import Attendance
from .serializers import AttendanceSerializer


class MyAttendanceView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):

        student = Student.objects.get(
            user=request.user,
            status="ACTIVE",
        )

        attendance = Attendance.objects.filter(
            student=student,
        ).order_by("-joined_at")

        serializer = AttendanceSerializer(
            attendance,
            many=True,
        )

        return success_response(
            data=serializer.data,
            message="Attendance fetched successfully.",
        )