"""kollegecliq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login/', views.loginregister,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('blog/', views.blog),
    path('about/', views.about),
    path('contact/', views.contact_us,name='conatct'),
    path('wishlist/', views.wishlist),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('edit-profile/',views.edit_profile, name='edit-profile'),
    path('Register-college/', views.register_college),
    path('Register-user/', views.register_user),
    path('forgot-password/', views.forgot_password),
    path('change-password/', views.change_password),
    path('college-detail/', views.college_detail),
    path('apply/', views.apply),
    path('login/checkuser/', views.loginregister),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    
]
