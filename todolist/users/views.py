"""Views for the users app."""

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    """View for user registration."""

    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """Custom token obtain view."""

    permission_classes = [AllowAny]
