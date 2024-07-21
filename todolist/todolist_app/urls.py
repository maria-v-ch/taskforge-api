from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (TaskViewSet, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView, TagViewSet)


app_name = 'tasks'

router = DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('tags', TagViewSet)


urlpatterns = [
   path('', include(router.urls)),
   # path('comments/create/', CommentCreateAPIView.as_view()),
   # path('comments/', CommentListAPIView.as_view()),
   # path('comments/<int:pk>/', CommentRetrieveAPIView.as_view()),
   # path('comments/<int:pk>/update/', CommentUpdateAPIView.as_view()),
   # path('comments/<int:pk>/delete/', CommentDestroyAPIView.as_view()),
   path('comments/', CommentListCreateAPIView.as_view()),
   path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
]
