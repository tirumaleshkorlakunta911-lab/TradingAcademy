from rest_framework.permissions import BasePermission
from apps.subscriptions.models import PremiumSubscription


class IsPremiumSubscriber(BasePermission):

    message = "You need an active Premium Tips subscription."

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        return PremiumSubscription.objects.filter(
            user=request.user,
            status="ACTIVE",
        ).exists()

class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_staff
        )


class IsStudent(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.user_type == "STUDENT"
        )


class IsPremiumUser(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_premium
        )