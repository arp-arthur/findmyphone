from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .serializers import CreateUserSerializer, UserTokenSerializer, UserSerializer

# Create your views here.

class CreateUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        token = Token.objects.create(user=serializer.instance)
        token_data = {"token": token.key}

        return Response(
            {**serializer.data, **token_data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
    

class LoginUserAPIView(APIView):
    serializer_class = UserTokenSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None) -> Response:
        serializer = UserTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data.get("username"), password=serializer.data.get("password"))

            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            
            return Response({"message": "Wrong credentials. Please try again"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None) -> Response:
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        
        return User.objects.filter(user=self.request.user)