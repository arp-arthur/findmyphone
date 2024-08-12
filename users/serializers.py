from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.contrib.auth.models import User

class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, max_length=255)
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    name = serializers.CharField(source="userprofile.name", required=False)
    photo_url = serializers.CharField(source="userprofile.photo_url", required=False)

    class Meta:
        model = get_user_model()
        fields = (
            "name",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "photo_url"
        )

        extra_kwargs = {
            "password": {"write_only": True},
            "is_staff": {"read_only": True},
            "is_superuser": {"read_only": True},
            "is_active": {"read_only": True}
        }

    def create(self, validated_data):
        profile_data = validated_data.pop("userprofile", {})
        user = get_user_model().objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user
    
class UserTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email"
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "name",
            "photo_url"
        )