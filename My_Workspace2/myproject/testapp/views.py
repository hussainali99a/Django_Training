from django.shortcuts import render
from django.http import HttpResponse


def greeting(request):
    s = "Hello and Welcome to  my First Project"
    return HttpResponse(s)

def myclass(request):
    v = "This is my AI-DS class"
    return HttpResponse(v)
# Create your views here.