from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def testpaper(request):
    question1 = "Who developed python?"
    a = "Dennis Ritchie"
    b = "Mustafa"
    c = "Nikhlesh"
    d = "Pankaj"
    e = "Guide Ven Rossum"

    # question2 = "Who developed c++?"
    # a1 = "Dennis Ritchie"
    # b1 = "Mustafa"
    # c1= "Nikhlesh"
    # d1 = "Pankaj"
    # e1 = "Guide Ven Rossum"

    # question3 = "Who developed java?"
    # a2 = "Dennis Ritchie"
    # b2 = "Mustafa"
    # c2 = "Nikhlesh"
    # d2 = "Pankaj"
    # e2 = "Guide Ven Rossum"
    context = {
        'question1':question1,
        'options':[a,b,c,d,e]

        # 'question2':question2,
        # 'a1':a1,
        # 'b1':b1,
        # 'c1':c1,
        # 'd1':d1,
        # 'e1':e1,

        # 'question3':question3,
        # 'a2':a2,
        # 'b2':b2,
        # 'c2':c2,
        # 'd2':d2,
        # 'e2':e2,
    }

    template = loader.get_template('testpaper.html')
    res = template.render(context,request)
    return HttpResponse(res)