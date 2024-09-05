from django.shortcuts import render
from detailsapp.models import Book
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    res = template.render()
    return HttpResponse(res)

def store(request):
    template = loader.get_template('store.html')
    res = template.render(request=request)
    return HttpResponse(res)

def bookentry(request):
    if request.method =='POST':
        book=Book()
        book.bname = request.POST['bookname']
        book.bprice = request.POST['bookprice']
        
        book.save()
        return HttpResponseRedirect('/')
    
def get_books(request):
        
        book=Book.objects.all().values()
        lis = list(book)
        template = loader.get_template('get.html')
        res = template.render(context={'books':lis})
        return HttpResponse(res)
