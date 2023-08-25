from django.contrib import admin
from django.urls import path, include 
from todo_app.views import index, bye, hello 

urlpatterns = [
    path('index/', index, name='todo_index'),
    path('bye/', bye, name='todo_bye'),
    path('hello/', hello, name='todo_hello'),
]
