from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    s="<h1>This is Home page</h1>"
    return HttpResponse(s)
def about(request):
    a="<h1>This is About page</h1>"
    return HttpResponse(a)
    
def contact(request):
    b="<h1>This is Contact page</h1>"
    return HttpResponse(b)
