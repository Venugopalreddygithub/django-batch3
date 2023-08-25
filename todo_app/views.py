from django.shortcuts import redirect, render 
from django.http import HttpResponse 


def index(request):
    return HttpResponse("Index function")

def bye(request):
    return HttpResponse("Bye function")

def hello(request):
    return HttpResponse("Hello function")