from django.db.models import Q
from apps.students.models import Student
from apps.subscriptions.models import PremiumSubscription

from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.responses import success_response

from .models import Announcement
from .serializers import AnnouncementSerializer


class AnnouncementListView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):

        user = request.user

        targets = ["ALL"]

        # Check Student
        if Student.objects.filter(
            user=user,
            status="ACTIVE",
        ).exists():
            targets.append("STUDENT")

        # Check Premium Subscription
        if PremiumSubscription.objects.filter(
            user=user,
            status="ACTIVE",
        ).exists():
            targets.append("PREMIUM")

        announcements = Announcement.objects.filter(
            is_active=True,
            publish_at__lte=timezone.now(),
            target_audience__in=targets,
        ).order_by("-publish_at")

        serializer = AnnouncementSerializer(
            announcements,
            many=True,
        )

        return success_response(
            data=serializer.data,
            message="Announcements fetched successfully.",
        )


class AnnouncementDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, pk):

        announcement = get_object_or_404(
            Announcement,
            pk=pk,
            is_active=True,
        )

        serializer = AnnouncementSerializer(
            announcement,
        )

        return success_response(
            data=serializer.data,
            message="Announcement fetched successfully.",
        )