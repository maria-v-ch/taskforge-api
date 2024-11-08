"""URL configuration for the todolist app."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, TagViewSet, TaskViewSet

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="task")
router.register("comments", CommentViewSet, basename="comment")
router.register("tags", TagViewSet, basename="tag")

urlpatterns = [
    path("", include(router.urls)),
]
