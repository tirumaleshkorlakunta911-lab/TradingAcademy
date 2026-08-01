from rest_framework.permissions import BasePermission

from .models import Student


class IsStudent(BasePermission):

    message = "Only students can access this resource."

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        return Student.objects.filter(
            user=request.user,
            status="ACTIVE",
        ).exists()