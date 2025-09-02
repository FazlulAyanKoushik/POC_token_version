from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, UserLoginSerializer, RefreshSerializer
from django.contrib.auth import login, logout
from rest_framework import status, permissions
from .utils import get_tokens_for_user
from .models import User
from django.conf import settings
import jwt


class UserLogin(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        user.token_version += 1
        user.save()
        token = get_tokens_for_user(user)
        return Response(token, status=status.HTTP_200_OK)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        user.token_version += 1
        user.save()
        return Response({
            "msg": "Successfully logged out"
        },status=status.HTTP_204_NO_CONTENT)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
