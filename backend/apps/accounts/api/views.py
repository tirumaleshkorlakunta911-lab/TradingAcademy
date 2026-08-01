from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "success": True,
                    "message": "User registered successfully.",
                    "data": {
                        "id": serializer.instance.id,
                        "email": serializer.instance.email,
                        "full_name": serializer.instance.full_name,
                    },
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )