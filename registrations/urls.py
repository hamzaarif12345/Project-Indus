"""registration URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from app1 import views
from app1 import views
from app1 import forms
from django.urls import path
from app1.views import create_todo
from app1.views import my_form,my_form1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    #path('forms/', forms, name='forms'),
    path('create/', create_todo, name='create'),
    path('message_create/',views.message_create, name='message_create'),
    path('home/my_form',views.my_form,name='my_form'),
    path('home/my_form1',views.my_form1, name='my_form1')
    
]