from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .auth_serializers import LoginSerializer


class LoginView(APIView):

    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data["user"]

            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "success": True,
                    "message": "Login successful.",
                    "data": {
                        "access": str(refresh.access_token),
                        "refresh": str(refresh),
                        "user": {
                            "id": user.id,
                            "full_name": user.full_name,
                            "email": user.email,
                            "user_type": user.user_type,
                            "is_premium": user.is_premium,
                        },
                    },
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                "success": False,
                "message": "Login failed.",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )