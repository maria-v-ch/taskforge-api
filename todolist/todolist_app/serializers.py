"""Serializers for the todolist app."""

from rest_framework import serializers

from .models import Comment, Tag, Task


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""

    author_email = serializers.EmailField(source="author.email", read_only=True)

    class Meta:
        """Meta options for CommentSerializer."""

        model = Comment
        fields = ["id", "text", "created_at", "author_email"]
        read_only_fields = ["author", "task"]


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model."""

    class Meta:
        """Meta options for TagSerializer."""

        model = Tag
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model."""

    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
    tags = TagSerializer(many=True, required=False)
    owner_email = serializers.EmailField(source="owner.email", read_only=True)

    class Meta:
        """Meta options for TaskSerializer."""

        model = Task
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
            "due_date",
            "status",
            "owner_email",
            "comments_count",
            "comments",
            "tags",
        ]
        read_only_fields = ["owner"]
