from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CreatePremiumOrderSerializer


class CreatePremiumOrderView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CreatePremiumOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "success": True,
                "message": "Premium order created successfully.",
                "data": {
                    "amount": 999,
                    "currency": "INR",
                    "status": "PENDING",
                },
            }
        )