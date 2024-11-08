"""Admin configuration for the todolist app."""

from django.contrib import admin

from .models import Comment, Tag, Task


class CommentInline(admin.TabularInline):
    """Inline admin for comments.

    TabularInline displays related objects in a tabular format.
    StackedInline is an alternative that displays them as stacked blocks.
    """

    model = Comment
    extra = 0


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin configuration for Task model."""

    list_display = ("name", "status", "owner", "created_at", "due_date")
    search_fields = ("name", "description")
    list_filter = ("status", "owner", "created_at", "due_date")
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin configuration for Comment model."""

    list_display = ("text", "task", "created_at")
    search_fields = ("text", "task__name", "task__description")
    list_filter = ("task", "created_at")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin configuration for Tag model."""

    list_display = ("name",)
    search_fields = ("name",)
