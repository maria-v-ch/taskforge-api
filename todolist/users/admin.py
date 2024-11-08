"""Admin configuration for the users app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class ToDoUserAdmin(BaseUserAdmin):
    """Custom admin configuration for User model."""

    model = User
    list_display = (
        "email",
        "is_staff",
        "role",
        "is_active",
    )
    list_filter = (
        "role",
        "email",
        "is_staff",
        "is_active",
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, ToDoUserAdmin)
