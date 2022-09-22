import email
import re
from urllib import request
from django.shortcuts import render
import copy
import uuid
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.hashers import make_password
from mainapp.serializers import RegisterSerializer
from mainapp.models import RegisteredUsers
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
    message =''
    if request.method == "POST":
        if RegisteredUsers.objects.filter(username=request.POST['username']):
            message = 'User already exist.'
        else:
            data = copy.deepcopy(request.POST)
            print(data)
            if request.POST['username'] and request.POST['login-password1'] != '' and request.POST['login-password2'] != '' and request.POST['login-password1'] == request.POST['login-password2']:
                data['password'] = make_password(request.POST.get('login-password1'))
                data['user_id'] = str(uuid.uuid4())
                del data['login-password1']
                del data['login-password2']
                # import ipdb;ipdb.set_trace()
                serializer = RegisterSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    message = 'Registration successful.'
                    # return render(request,'kollegecliq/registeruser.html') 
            else:
                if request.POST['username'] and request.POST['login-password1'] == '' and request.POST['login-password2'] == '':                   
                    print("working")
                    serializer = RegisterSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        message = 'Registration successful.'
        
    return render(request,'kollegecliq/registeruser.html',context={'message':message})

def forgot_password(request):
    return render(request,'kollegecliq/forgot-password.html')

def college_detail(request):
    return render(request,'kollegecliq/collegedetail.html')

def apply(request):
    return render(request,'kollegecliq/apply.html')


###################### Suppotive function ############################################

