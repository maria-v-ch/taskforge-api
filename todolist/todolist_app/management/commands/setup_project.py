"""Management command to setup the project."""

from typing import Any

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection

User = get_user_model()


class Command(BaseCommand):
    """Setup project command."""

    help = "Setup project: create database, run migrations, create superuser"

    def handle(self, *args: Any, **kwargs: Any) -> None:
        """Execute the command.

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        self.stdout.write("Setting up project...")

        # Drop database if it exists
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT pg_terminate_backend(pg_stat_activity.pid) "
                    "FROM pg_stat_activity "
                    "WHERE pg_stat_activity.datname = 'todolist' "
                    "AND pid <> pg_backend_pid();"
                )
                cursor.execute("DROP DATABASE IF EXISTS todolist")
                cursor.execute("CREATE DATABASE todolist")
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Database operation failed: {e}"))

        # Run migrations
        self.stdout.write("Running migrations...")
        call_command("makemigrations")
        call_command("migrate")

        # Create superuser if it doesn't exist
        if not User.objects.filter(email="admin@example.com").exists():
            self.stdout.write("Creating superuser...")
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123",
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "Superuser created successfully:\n"
                    "Email: admin@example.com\n"
                    "Password: admin123"
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                "\nProject setup completed successfully!\n"
                "You can now run the server with: python manage.py runserver"
            )
        )
