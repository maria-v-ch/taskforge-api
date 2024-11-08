"""Views for the todolist app."""

from typing import Any

from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

from .models import Comment, Tag, Task
from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, TagSerializer, TaskSerializer


def base(request: HttpRequest) -> HttpResponse:
    """Render base template with all tasks."""
    tasks = Task.objects.all()
    return render(request, "todolist_app/base.html", {"tasks": tasks})


class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing tasks."""

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["status"]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "due_date", "status"]

    def get_queryset(self) -> models.QuerySet[Task, Task]:
        """Return tasks for the current user."""
        if not self.request.user.is_authenticated:
            return Task.objects.none()
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer: BaseSerializer[Any]) -> None:
        """Save the owner when creating a task."""
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["post"])
    def add_comment(self, request: Request, pk: int | None = None) -> Response:
        """Add a comment to a task."""
        task = self.get_object()
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(task=task, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing comments."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self) -> models.QuerySet[Comment, Comment]:
        """Return comments for tasks owned by the current user."""
        if not self.request.user.is_authenticated:
            return Comment.objects.none()
        return Comment.objects.filter(task__owner=self.request.user)

    def perform_create(self, serializer: BaseSerializer[Any]) -> None:
        """Save the author when creating a comment."""
        serializer.save(author=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing tags."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
