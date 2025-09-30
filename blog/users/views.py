from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer


class RegisterUserAPIView(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # token retrieval
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "message": "User created successfully",
                    "username": user.username,
                    "token": token.key
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
