"""Configuration for the todolist app."""

from django.apps import AppConfig


class TodolistAppConfig(AppConfig):
    """Configuration class for the todolist app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "todolist_app"
