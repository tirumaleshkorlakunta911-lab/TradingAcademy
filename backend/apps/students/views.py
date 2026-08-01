from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .permissions import IsStudent
from .serializers import StudentSerializer


class StudentProfileView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsStudent,
    ]

    def get(self, request):

        student = Student.objects.get(
            user=request.user
        )

        serializer = StudentSerializer(student)

        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )

class StudentDashboardView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsStudent,
    ]

    def get(self, request):

        student = Student.objects.get(user=request.user)

        data = {
            "student": {
                "student_id": student.student_id,
                "name": request.user.full_name,
                "email": request.user.email,
                "status": student.status,
                "batch": student.batch_name,
                "mentor": student.mentor_name,
                "course_start_date": student.course_start_date,
                "course_end_date": student.course_end_date,
            },

            "dashboard": {
                "join_live_class": True,
                "recordings": True,
                "study_materials": True,
                "attendance": True,
                "announcements": True,
                "premium_tips": True,
            }
        }

        return Response(
            {
                "success": True,
                "data": data
            }
        )