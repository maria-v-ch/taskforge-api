"""Models for the todolist app."""

from typing import Any

from django.db import models
from django.utils import timezone
from users.models import User


class Task(models.Model):
    """Task model for the TODO list application."""

    STATUS_CHOICES: list[tuple[str, str]] = [
        ("DRAFT", "Draft"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
        ("ARCHIVED", "Archived"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="DRAFT")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    class Meta:
        """Meta options for Task model."""

        ordering = ["-created_at"]

    def __str__(self) -> str:
        """Return string representation of Task."""
        return f"{self.name} ({self.status})"

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Save the task with updated timestamp."""
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class Comment(models.Model):
    """Comment model for tasks."""

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    class Meta:
        """Meta options for Comment model."""

        ordering = ["-created_at"]

    def __str__(self) -> str:
        """Return string representation of Comment."""
        return f"Comment by {self.author.email} on {self.task.name}"


class Tag(models.Model):
    """Tag model for tasks."""

    name = models.CharField(max_length=50, unique=True)
    tasks = models.ManyToManyField(Task, related_name="tags")

    def __str__(self) -> str:
        """Return string representation of Tag."""
        return str(self.name)
