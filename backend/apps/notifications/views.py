from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.responses import success_response
from django.shortcuts import get_object_or_404

from .models import Notification
from .serializers import NotificationSerializer


class NotificationListView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):

        notifications = Notification.objects.filter(
            user=request.user,
        )

        serializer = NotificationSerializer(
            notifications,
            many=True,
        )

        return success_response(
            data=serializer.data,
            message="Notifications fetched successfully.",
        )

class MarkNotificationReadView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def patch(self, request, pk):

        notification = get_object_or_404(
            Notification,
            pk=pk,
            user=request.user,
        )

        notification.is_read = True
        notification.save()

        return success_response(
            message="Notification marked as read.",
        )

class UnreadNotificationCountView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):

        count = Notification.objects.filter(
            user=request.user,
            is_read=False,
        ).count()

        return success_response(
            data={
                "unread_count": count,
            },
            message="Unread count fetched successfully.",
        )

class MarkAllNotificationsReadView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def patch(self, request):

        Notification.objects.filter(
            user=request.user,
            is_read=False,
        ).update(
            is_read=True,
        )

        return success_response(
            message="All notifications marked as read.",
        )