from django.shortcuts import redirect, render 
from django.http import HttpResponse, JsonResponse 
from todo_app.models import Todo 

def index(request):
    todo = Todo.objects.last()
    html = f"""
        <h1>Hello World </h1>
        <p>Bye</p>
        <p>Todod title: {todo.title}</p>
""" 
    return HttpResponse(html)

def bye(request):
    todo = Todo.objects.last()
    a = { 
        "title": todo.title,
        "author": "Nepoleon Hill"
    }
    return JsonResponse(a)

def hello(request):
    todos = Todo.objects.all()
    page_name = "temp.html"
    return render(request, page_name, context={'todos': todos, 'show': True})