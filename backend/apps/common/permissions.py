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