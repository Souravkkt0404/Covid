"""django_pro URL Configuration

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
from app_one.views import *

urlpatterns = [
    path('index/',index),
    path('login/test_run',login_auth),
    path('login/',login),
    path('reg/',reg),
    path('covid/',covid),
    path('reg/register',register),
    path('test_page/',test_return),
    path('logout/',logout,name='login-page'),
    path('login_ws/',login_ws),
    path('login_ws/login_val',login_validation),
]
