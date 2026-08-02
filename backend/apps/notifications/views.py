from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.responses import success_response

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