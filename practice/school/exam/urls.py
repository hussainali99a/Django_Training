from django.urls import path
from exam import views



urlpatterns = [
    path('quiz/',views.testpaper),
    path('result/',views.result),
]