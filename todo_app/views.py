from django.shortcuts import redirect, render 
from django.http import HttpResponse, JsonResponse 
from todo_app.models import Todo


def index(request):
    all_todos = Todo.objects.all()
    data = {
        "todo": all_todos
    }
    return render(request, "index.html", context=data)