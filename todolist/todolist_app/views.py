from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


# def base(request):
#     tasks = Task.objects.all()
#     return render(request, 'todolist_app/base.html', {'tasks': tasks})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
