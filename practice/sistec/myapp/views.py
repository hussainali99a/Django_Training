from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    res = template.render()
    return HttpResponse(res)

def python(request):
    template = loader.get_template('python.html')
    res = template.render()
    return HttpResponse(res)

def cpp(request):
    template = loader.get_template('cpp.html')
    res = template.render()
    return HttpResponse(res)

def java(request):
    template = loader.get_template('java.html')
    res = template.render()
    return HttpResponse(res)

def javascript(request):
    template = loader.get_template('javascript.html')
    res = template.render()
    return HttpResponse(res)

def r(request):
    template = loader.get_template('r.html')
    res = template.render()
    return HttpResponse(res)

