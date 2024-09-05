from django.urls import path
from detailsapp import views
app_name = 'detailsapp'
urlpatterns =[
    path('',views.home ,name = 'home'),
    
    path('store/',views.store ,name = 'store'),
    path('bookentry/',views.bookentry ,name = 'bookentry'),
    path('get/',views.get_books,name = 'get')
    
]