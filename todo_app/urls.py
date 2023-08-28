from django.contrib import admin
from django.urls import path, include 
from todo_app.views import index, add_view, detailed_view, delete_todo, mark_view
urlpatterns = [
    path('', index, name='todo_index'),
    path('add-todo/', add_view, name='add-todo'),
    path('detailed-view/<int:todo_id>/', detailed_view, name='detailed_view'),
    path('delete-todo/<int:todo_id>', delete_todo, name="delete_todo"),
    path('mark-view/<int:todo_id>', mark_view, name='mark_view')
]
