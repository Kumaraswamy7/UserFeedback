
from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name='index'),
    path('index',index2,name='index2'),
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('home',home,name='home'),
    path('feedback',feedback,name='feedback'),
    path('thanku',thanku,name='thanku'),
]
