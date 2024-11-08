"""Models for the users app."""

from typing import TypeVar

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

UserType = TypeVar("UserType", bound="User")


class CustomUserManager(UserManager["User"]):
    """Custom manager for User model."""

    use_in_migrations = True

    def _create_user(
        self,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
        **extra_fields: bool | str | None,
    ) -> "User":
        """Create and save a user with the given email and password."""
        if not email:
            raise ValueError("The email field must be set")
        email = self.normalize_email(email)
        # Use email as username if not provided
        if not username:
            username = email
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
        **extra_fields: bool | str | None,
    ) -> "User":
        """Create and save a regular user."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(
        self,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
        **extra_fields: bool | str | None,
    ) -> "User":
        """Create and save a superuser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    """Custom user model."""

    USERNAME_FIELD = "email"  # type: ignore[assignment]
    REQUIRED_FIELDS = ["username"]  # type: ignore[assignment]
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("guide", "Guide"),
        ("user", "User"),
    )

    # Model fields
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        "email",
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    phone = models.CharField(
        "phone",
        max_length=12,
        unique=True,
        null=True,
        blank=True,
    )
    role = models.CharField(
        "role",
        max_length=10,
        choices=ROLE_CHOICES,
        null=True,
        blank=True,
    )

    # Manager
    objects = CustomUserManager()  # type: ignore[assignment]

    def __str__(self) -> str:
        """Return string representation of User."""
        return str(self.email)

    class Meta:
        """Meta options for User model."""

        verbose_name = "user"
        verbose_name_plural = "users"
