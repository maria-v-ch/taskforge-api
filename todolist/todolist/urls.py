"""URL configuration for todolist project."""

from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from todolist_app.views import CommentViewSet, TagViewSet, TaskViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="task")
router.register("comments", CommentViewSet, basename="comment")
router.register("tags", TagViewSet, basename="tag")

schema_view = get_schema_view(
    openapi.Info(
        title="TodoList API",
        default_version="v1",
        description="API for managing todo lists",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@todolist.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/users/", include("users.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
