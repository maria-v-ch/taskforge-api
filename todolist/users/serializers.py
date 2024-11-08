"""Serializers for the users app."""

from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""

    password = serializers.CharField(write_only=True)

    class Meta:
        """Meta options for RegisterSerializer."""

        model = User
        fields = ("email", "password")

    def create(self, validated_data: dict) -> User:
        """Create and return a new user.

        Args:
            validated_data: Dictionary of validated user data

        Returns:
            User: Created user instance
        """
        return User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
