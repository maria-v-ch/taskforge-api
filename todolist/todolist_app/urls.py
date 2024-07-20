from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (TaskViewSet, CommentCreateView, CommentListView, CommentRetrieveView, CommentUpdateView,
                    CommentDestroyView, TagViewSet)


app_name = 'tasks'

router = DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('tags', TagViewSet)


urlpatterns = [
   path('', include(router.urls)),
   path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
   path('comments/', CommentListView.as_view(), name='comment-list'),
   path('comments/<int:pk>/', CommentRetrieveView.as_view(), name='comment-retrieve'),
   path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
   path('comments/<int:pk>/delete/', CommentDestroyView.as_view(), name='comment-destroy'),
]
