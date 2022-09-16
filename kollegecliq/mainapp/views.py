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