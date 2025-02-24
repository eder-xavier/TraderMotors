from django.urls import path 
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'MainTM'

urlpatterns = [
    path('', views.home,  name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]