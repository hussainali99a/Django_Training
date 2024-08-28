from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testpaper(request):
    s="<h1>This is a Testpaper page</h1>"
    return HttpResponse(s)
def result(request):
    s="<h1>This is a Result page</h1>"
    return HttpResponse(s)

