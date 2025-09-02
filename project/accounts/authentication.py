# users/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions
from django.contrib.auth import get_user_model

User = get_user_model()

class VersionedJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user: User = super().get_user(validated_token)
        token_version = validated_token.get("token_version")

        if token_version is None or token_version != user.token_version:
            print(token_version, user.token_version)
            raise exceptions.AuthenticationFailed("Token is invalid or expired")

        return user
