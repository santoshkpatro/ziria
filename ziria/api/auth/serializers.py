from rest_framework import serializers

from ziria.models.store import Store
from ziria.models.user import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    full_name = serializers.CharField()
    password = serializers.CharField()


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("id", "name", "slug", "country")


class LoginProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "full_name", "access_token", "refresh_token")
