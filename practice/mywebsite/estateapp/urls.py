from django.urls import path
from estateapp import views



urlpatterns = [
    path('estate/',views.estate),
]