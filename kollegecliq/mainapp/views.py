import email
from email import message
import re
from urllib import request
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect
import copy
import uuid
from django.contrib import messages
from datetime import datetime
from mainapp.serializers import RegisterSerializer,ContactSerializer,CollegeRegisterSerializer
from mainapp.models import RegisteredUsers,RegisteredCollege
from django.views.decorators.csrf import csrf_exempt
import base64
import string
import random

# Create your views here.
def index(request):
    return render(request,'kollegecliq/index.html')

@csrf_exempt
def loginregister(request):
    if request.method == 'POST':
        if RegisteredUsers.objects.filter(username=request.POST['username'].lower()):
            user = RegisteredUsers.objects.get(username=request.POST['username'].lower())
            if (user.password and not request.POST['password']):
                message = "required"
                return JsonResponse({"message":message}) 
            elif (user.password and request.POST['password']):
                if user.password == make_password(request.POST['password']):
                    request.session['user_id']= user.user_id
                    request.session['username']= user.username
                    return JsonResponse({"message":"ok",'type':'user'}) 
                else:
                    return JsonResponse({"message":"Incorrect username or password."})
            elif (not user.password and not request.POST['password']):
                request.session['user_id']= user.user_id
                request.session['username']= user.username
                return JsonResponse({"message":"ok"}) 
        elif RegisteredCollege.objects.filter(email=request.POST['username'].lower()) or RegisteredCollege.objects.filter(phone=request.POST['username']):            
            if not request.POST['password']:
                message = "required"
                return JsonResponse({"message":message})
            else:
                user = RegisteredCollege.objects.get(email=request.POST['username'].lower()) if RegisteredCollege.objects.filter(email=request.POST['username'].lower()) else RegisteredCollege.objects.get(phone=request.POST['username']) 
                print(user)
                if user.password == make_password(request.POST['password']):
                    request.session['user_id']= user.user_id
                    request.session['username']= user.email
                    return JsonResponse({"message":"ok"})
                else:
                    return JsonResponse({"message":"Incorrect username or password."})
        else:
            return JsonResponse({"message":"In-Valid Username."}) 
    return render(request,'kollegecliq/login.html')

def logout_user(request):
    if request.session.has_key('user_id'):
        del request.session['user_id']
        del request.session['username']
    return redirect('/login/')

def blog(request):
    return render(request,'kollegecliq/blog.html')

def about(request):
    return render(request,'kollegecliq/about.html')

def contact_us(request):
    message = ''
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            message = "Thank you for contacting us. We recieved your message."
    return render(request,'kollegecliq/contact.html',context={'message':message})

def wishlist(request):
    return render(request,'kollegecliq/wishlist.html')

def myaccount(request):
    if request.session.has_key('user_id'):
        user, type = (RegisteredUsers.objects.get(user_id = request.session['user_id']), 'user') if RegisteredUsers.objects.filter(user_id = request.session['user_id']) else (RegisteredCollege.objects.get(user_id = request.session['user_id']), 'college')
        return render(request, 'kollegecliq/myaccount.html', context={'user':user,'type':type})
    return redirect('/login/')

@csrf_exempt
def edit_profile(request):
    message = ''
    if request.session.has_key('user_id'):
        if request.method == 'POST':
            if (request.POST['currentpassword'] != '' and (request.POST['password1'] == request.POST['password2']) or (request.POST['currentpassword'] == '' and (request.POST['password1'] == request.POST['password2']))):
                user = RegisteredUsers.objects.get(user_id=request.session['user_id'])
                if user.password:
                    if request.POST['currentpassword']:
                        if make_password(request.POST['currentpassword']) == user.password:
                            user.name = request.POST['name']
                            user.username = request.POST['username'] 
                            user.email = request.POST['email']
                            user.phone = request.POST['phone']
                            user.password = make_password(request.POST['password2']) 
                            user.updated_on = datetime.now()
                            user.save()
                            message = "Profile updated successfully."
                        else:
                            message = "Current Password don't match."   
                else:
                    if request.POST['currentpassword']:
                        message = "Current Password don't match."
                    else:
                        user.name = request.POST['name']
                        user.username = request.POST['username'] 
                        user.email = request.POST['email']
                        user.phone = request.POST['phone'] 
                        user.password = make_password(request.POST['password2']) 
                        user.updated_on = datetime.now()
                        user.save()
                        message = "Profile updated successfully."
                    
            elif request.POST['currentpassword'] == '':
                message = "Current password is required."  
                         
            else:
                message = "Password don't match."
        else:
            message = "Invalid request."
    else:
        message = "Invalid request."
    return JsonResponse({"message":message})

def register_college(request):
    message = ''
    if request.method == "POST":
        if RegisteredCollege.objects.filter(email=request.POST['email'].lower()) or RegisteredCollege.objects.filter(phone=request.POST['phone']):
            message = 'College already exist.'
        else:
            data = copy.deepcopy(request.POST)
            if data['phone'].isnumeric() and checkemail(data['email']) and data['password1'] == data['password2'] and data['password1'] != '' and data['password2'] != '':
                data['password'] = make_password(data['password1'])
                del data['password1']
                del data['password2']
                serializer = CollegeRegisterSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                otp = generateOtp()
                print(otp)
                request.session['clzemail']= data['email']
                request.session['clzphone']= data['phone']
                request.session['clzotp'] = otp
                # return render(request,'kollegecliq/otpverify.html',context={'message' : message,'name':data['name'],'email':data['email']}) 
                return render(request,'kollegecliq/otpverify.html',context={'message' : message,'type':'college'}) 
            else:
                message = "Please check your password."
        return render(request,'kollegecliq/registercollege.html',context={'message' : message,'data':request.POST})
    return render(request,'kollegecliq/registercollege.html',context={'message' : message})

def register_user(request):
    message =''
    if request.method == "POST":
        if RegisteredUsers.objects.filter(username=request.POST['username'].lower()):
            message = 'User already exist.'
        else:
            data = copy.deepcopy(request.POST)
            data['username'] = data['username'].lower()
            if data['username'].isnumeric() or checkemail(data['username']):
                data['phone'] = data['username'] if data['username'].isnumeric() else ''
                data['email'] = data['username'] if  checkemail(data['username']) else ''
                if request.POST['username'] and request.POST['login-password1'] != '' and request.POST['login-password2'] != '' and request.POST['login-password1'] == request.POST['login-password2']:
                    # import ipdb;ipdb.set_trace()
                    data['password'] = make_password(request.POST['login-password1'])
                    del data['login-password1']
                    del data['login-password2']                    
                    serializer = RegisterSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        # message = 'Registration successful.'                    
                    # return render(request,'kollegecliq/welcome.html',context={'message' : message,'name':data['name'],'email':data['email'] if data['email'] else data['phone']}) 
                else:
                    if request.POST['username'] and request.POST['login-password1'] == '' and request.POST['login-password2'] == '':                   
                        serializer = RegisterSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            # message = 'Registration successful.'
                otp = generateOtp()
                print(otp)
                request.session['user_username']= data['email'] if data['email'] else data['phone']
                request.session['userotp'] = otp            
                return render(request,'kollegecliq/otpverify.html',context={'message' : message,'type':'user'}) 
            else:
                message = "Please enter valid Username."
    return render(request,'kollegecliq/registeruser.html',context={'message':message})

def forgot_password(request):
    message = ''
    if request.method == 'POST':
        if checkemail(request.POST['username']):
            if RegisteredUsers.objects.filter(email = request.POST['username'].lower()):
                request.session['ch-username'] = request.POST['username']
                otp = generateOtp()
                print(otp)
                request.session['ch-otp'] = otp
                message = "OTP has been sent to your Email."
                return render(request,'kollegecliq/otpverify.html',context={'message':message,'type':'chpu'})
            else:
                message = "Sorry, No record found."

        elif request.POST['username'].isnumeric():
            if RegisteredUsers.objects.filter(phone = request.POST['username']):
                request.session['ch-username'] = request.POST['username']
                otp = generateOtp()
                print(otp)
                request.session['ch-otp'] = otp
                message = "OTP has been sent to your Phone."
                return render(request,'kollegecliq/otpverify.html',context={'message':message,'type':'chpu'})
            else:
                message = "Sorry, No record found"
        else:
            message = "Sorry, No record found."

    return render(request,'kollegecliq/forgot-password.html',context={'message':message})

def change_password(request):
    message = ''
    if request.method == 'POST':
        if (request.POST['password1'] == request.POST['password2']) and (request.POST['password1'] != "") and (request.POST['password2'] != ""):
            user = ''
            if (request.POST['type'] == 'chpu') and (RegisteredUsers.objects.filter(username=request.session['ch-username'])):
                user = RegisteredUsers.objects.get(username=request.session['ch-username'])
            elif (request.POST['type'] == 'chpc') and (RegisteredCollege.objects.filter(email=request.session['ch-username'])):
                user = RegisteredCollege.objects.get(email=request.session['ch-username'])
            user.password = make_password(request.POST['password1'])
            user.save()
            del request.session['ch-username']
            message = "Password updated."
        else:
            message = "Passwords do not matched."
            return render(request,'kollegecliq/change-password.html',context={'message':message,'type':request.POST['type']})
        return render(request,'kollegecliq/login.html', context={'message':message})
    return redirect('/login/')
    

def college_detail(request):
    return render(request,'kollegecliq/collegedetail.html')

def apply(request):
    return render(request,'kollegecliq/apply.html')

def verify_otp(request):
    message = ''
    if request.method == 'POST':
        otp = request.POST.get('otp')
        type = request.POST.get('type')
        if type == 'college':
            if request.session['clzotp'] == otp:
                user = RegisteredCollege.objects.get(email=request.session['clzemail'],phone=request.session['clzphone'])
                user.is_live = '1'
                user.save()
                message = 'Registration Successful.'
                del request.session['clzemail']
                del request.session['clzphone']
                del request.session['clzotp']
                return render(request,'kollegecliq/login.html',context={'message' : message})
                # return redirect('/login/') 
            else:
                message = "Wrong OTP! Please resend."
                return render(request,'kollegecliq/otpverify.html',context={'message' : message})
        elif type == 'user':
            if request.session['userotp'] == otp:
                user = RegisteredUsers.objects.get(username=request.session['user_username'])
                user.is_live = '1'
                user.save()
                message = 'Registration Successful.'
                del request.session['user_username']
                del request.session['userotp']
                return render(request,'kollegecliq/login.html',context={'message' : message})
                # return redirect('/login/') 
            else:
                message = "Wrong OTP! Please resend."
                return render(request,'kollegecliq/otpverify.html',context={'message' : message})
        elif type == 'chpu':
            if request.session['ch-otp'] == otp:
                del request.session['ch-otp']
                return render(request,'kollegecliq/change-password.html',context={'message' : message, 'type':'chpu'})
                # return redirect('/login/') 
            else:
                message = "Wrong OTP! Please resend."
                return render(request,'kollegecliq/otpverify.html',context={'message' : message, 'type':'chpu'})
        elif type == 'chpc':
            if request.session['chc-otp'] == otp:
                del request.session['chc-otp']
                return render(request,'kollegecliq/change-password.html',context={'message' : message, 'type':'chpc'})
                # return redirect('/login/') 
            else:
                message = "Wrong OTP! Please resend."
                return render(request,'kollegecliq/otpverify.html',context={'message' : message, 'type':'chpc'})
    return redirect('/login/')

def resend_otp(request):
    pass
###################### Suppotive function ############################################

def checkemail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def make_password(pwd):
    sample_string_bytes = pwd.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

def generateOtp():
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=6))
    return res