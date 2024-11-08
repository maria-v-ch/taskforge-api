"""Custom permissions for the todolist app."""

from typing import cast

from django.contrib.auth.models import AbstractUser
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

from .models import Task


class BasePermission(permissions.BasePermission):
    """Base permission class for all custom permissions."""

    def has_permission(self, request: Request, view: APIView) -> bool:
        """Check if user has permission to access view."""
        return bool(request.user and request.user.is_authenticated)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Permission to only allow owners of an object to edit it."""

    def has_permission(self, request: Request, view: APIView) -> bool:
        """Check if user has permission to access view."""
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request: Request, view: APIView, obj: Task) -> bool:
        """Check if user has permission to access object."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(obj.owner == request.user)


class CanEdit(permissions.BasePermission):
    """Permission to check if user can edit object."""

    def has_object_permission(self, request: Request, view: APIView, obj: Task) -> bool:
        """Check if user has edit permission."""
        user = cast(AbstractUser, request.user)
        return bool(
            user.is_staff
            or obj.owner == user
            or user.has_perm("todolist_app.change_task")
        )
