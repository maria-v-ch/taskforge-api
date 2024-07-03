from django.shortcuts import render
from .models import Task


def base(request):
    tasks = Task.objects.all()
    return render(request, 'todolist_app/base.html', {'tasks': tasks})
