from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .profile_serializers import UserProfileSerializer


class UserProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = UserProfileSerializer(request.user)

        return Response(
            {
                "success": True,
                "message": "Profile fetched successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )