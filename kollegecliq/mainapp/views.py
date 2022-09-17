from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'kollegecliq/index.html')

def loginregister(request):
    return render(request,'kollegecliq/login.html')

def blog(request):
    return render(request,'kollegecliq/blog.html')

def about(request):
    return render(request,'kollegecliq/about.html')

def wishlist(request):
    return render(request,'kollegecliq/wishlist.html')

def myaccount(request):
    return render(request,'kollegecliq/myaccount.html')
    
def register_college(request):
    return render(request,'kollegecliq/registercollege.html')

def register_user(request):
    return render(request,'kollegecliq/registeruser.html')

def forgot_password(request):
    return render(request,'kollegecliq/forgot-password.html')

def college_detail(request):
    return render(request,'kollegecliq/collegedetail.html')

def apply(request):
    return render(request,'kollegecliq/apply.html')