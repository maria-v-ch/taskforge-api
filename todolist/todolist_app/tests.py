"""Tests for the todolist app."""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User

from .models import Comment, Tag, Task


class TodolistModelsTest(APITestCase):
    """Test module for Todolist models."""

    def setUp(self) -> None:
        """Set up test data."""
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

    def test_task_creation(self) -> None:
        """Test creating a task."""
        task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            owner=self.user,
        )
        self.assertEqual(str(task), "Test Task (DRAFT)")
        self.assertEqual(task.status, "DRAFT")

    def test_comment_creation(self) -> None:
        """Test creating a comment."""
        task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            owner=self.user,
        )
        comment = Comment.objects.create(
            task=task,
            text="Test Comment",
            author=self.user,
        )
        expected_str = f"Comment by {self.user.email} on {task.name}"
        self.assertEqual(str(comment), expected_str)

    def test_tag_creation(self) -> None:
        """Test creating a tag."""
        tag = Tag.objects.create(name="Test Tag")
        task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            owner=self.user,
        )
        task.tags.add(tag)
        self.assertEqual(str(tag), "Test Tag")
        self.assertEqual(task.tags.count(), 1)


class TodolistAPITest(APITestCase):
    """Test module for Todolist API."""

    def setUp(self) -> None:
        """Set up test data."""
        # Create user and get token
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        # Get token
        refresh = RefreshToken.for_user(self.user)
        # Use proper type annotation for RefreshToken
        self.access_token = str(refresh.access_token)  # type: ignore[attr-defined]
        # Set token in client
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        # Create test task
        self.task_data = {
            "name": "API Test Task",
            "description": "API Test Description",
            "status": "DRAFT",
        }
        self.task = Task.objects.create(owner=self.user, **self.task_data)

    def test_create_task(self) -> None:
        """Test creating a task via API."""
        url = reverse("task-list")
        new_task_data = {
            "name": "New API Task",
            "description": "New Description",
            "status": "DRAFT",
        }
        response = self.client.post(url, new_task_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(response.data["name"], "New API Task")

    def test_get_task_list(self) -> None:
        """Test getting list of tasks."""
        url = reverse("task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_get_task_detail(self) -> None:
        """Test getting task detail."""
        url = reverse("task-detail", args=[self.task.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.task_data["name"])

    def test_update_task(self) -> None:
        """Test updating a task."""
        url = reverse("task-detail", args=[self.task.pk])
        updated_data = {
            "name": "Updated Task",
            "status": "IN_PROGRESS",
        }
        response = self.client.patch(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Task")
        self.assertEqual(response.data["status"], "IN_PROGRESS")

    def test_delete_task(self) -> None:
        """Test deleting a task."""
        url = reverse("task-detail", args=[self.task.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_add_comment_to_task(self) -> None:
        """Test adding a comment to a task."""
        url = reverse("task-add-comment", args=[self.task.pk])
        comment_data = {"text": "Test Comment"}
        response = self.client.post(url, comment_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.task.comments.count(), 1)
        comment = self.task.comments.first()
        if comment:
            self.assertEqual(comment.text, "Test Comment")
            self.assertEqual(comment.author, self.user)

    def test_unauthorized_access(self) -> None:
        """Test unauthorized access to API."""
        self.client.credentials()  # Remove credentials
        url = reverse("task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
