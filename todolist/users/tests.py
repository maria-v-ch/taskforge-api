"""Tests for the users app."""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class UserModelTests(TestCase):
    """Test module for User model."""

    def setUp(self) -> None:
        """Set up test data."""
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            role="user",
        )
        self.admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin123",
        )

    def test_create_user(self) -> None:
        """Test creating a regular user."""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self) -> None:
        """Test creating a superuser."""
        self.assertEqual(self.admin_user.email, "admin@example.com")
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)

    def test_user_str_method(self) -> None:
        """Test string representation of user."""
        self.assertEqual(str(self.user), "test@example.com")


class AuthenticationTests(APITestCase):
    """Test module for Authentication API views."""

    def setUp(self) -> None:
        """Set up test data."""
        self.user_data = {
            "email": "test@example.com",
            "password": "testpass123",
        }
        self.user = User.objects.create_user(
            username="testuser",
            email=self.user_data["email"],
            password=self.user_data["password"],
        )
        self.register_url = reverse("register")
        self.token_url = reverse("token_obtain_pair")

    def test_user_registration(self) -> None:
        """Test user registration endpoint."""
        data = {
            "email": "newuser@example.com",
            "password": "newpass123",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="newuser@example.com").exists())

    def test_user_login(self) -> None:
        """Test user login endpoint."""
        response = self.client.post(self.token_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_invalid_login(self) -> None:
        """Test login with invalid credentials."""
        invalid_data = {
            "email": "test@example.com",
            "password": "wrongpass",
        }
        response = self.client.post(self.token_url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
