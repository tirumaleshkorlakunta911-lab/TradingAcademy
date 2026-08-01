from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Tip
from .serializers import TipSerializer

from rest_framework.permissions import IsAuthenticated

from apps.common.permissions import IsPremiumSubscriber


class FreeTipListView(APIView):

    def get(self, request):

        tips = Tip.objects.filter(
            access_type="FREE",
            status="ACTIVE",
        ).order_by("-created_at")

        serializer = TipSerializer(tips, many=True)

        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )

class PremiumTipListView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsPremiumSubscriber,
    ]

    def get(self, request):

        category = request.GET.get("category")

        tips = Tip.objects.filter(
            access_type="PREMIUM",
            category=category,
            status="ACTIVE",
        ).order_by("-created_at")

        serializer = TipSerializer(
            tips,
            many=True,
        )

        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )