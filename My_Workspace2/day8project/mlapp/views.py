from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib

# Create your views here.
def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())

def result(request):
    cls = joblib.load('glassmlmodel.sav')
    lis = []
    lis.append(request.GET['RI'])
    lis.append(request.GET['Na'])
    lis.append(request.GET['Mg'])
    lis.append(request.GET['Al'])
    lis.append(request.GET['Si'])
    lis.append(request.GET['K'])
    lis.append(request.GET['Ca'])
    lis.append(request.GET['Ba'])
    lis.append(request.GET['Fe'])
    
    ans = cls.predict([lis])
    
    return render(request,'result.html',{'ans':ans ,'lis':lis})

