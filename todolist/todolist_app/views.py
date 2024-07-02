from django.shortcuts import render


def base(request):
    return render(request, 'todolist_app/base.html')
