from django.shortcuts import redirect, render 
from django.http import HttpResponse, JsonResponse 


def index(request):
    html = """
        <h1>Hello World </h1>
        <h6>Heading - 6 </h1>
        <p>Byee</P>
"""
    return HttpResponse(html)

def bye(request):
    a = { 
        "title": "Think and Grow Rich",
        "author": "Nepoleon Hill"
    }
    return JsonResponse(a)

def hello(request):
    page_name = "temp.html"
    return render(request, page_name)