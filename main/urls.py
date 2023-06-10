from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/login', include('user.urls'), name='login'),
    path('user/register', include('user.urls'), name='register'),
]
