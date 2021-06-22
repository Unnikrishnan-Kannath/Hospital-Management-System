#from hospital.app_hospital.models import user
from django.http import request
from django.db import models
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    return render(request,'index.html')

#sighn-up page render

def sighn(request):
    return render(request,'registration/sighnup.html')

#contact page render

def contact(request):
    return render(request,'contactus.html')

#login page render

def login(request):
    return render(request,'registration/login.html')

def signup_req(request):
	if request.method=="POST":
		first_name=request.POST.get('first_name')
		user_name=request.POST.get('username')
		email=request.POST.get('email')
		password=request.POST.get('psw')
		repeat_password=request.POST.get('psw-repeat')
		user=User.objects.create_user(username=user_name,password=password,email=email,first_name=first_name)
		user.save()
		print("User Created")
		return redirect('login')

	else:
		return render(request,'registration/signup.html')

def ip_data(request):
	user_email=request.POST.get('user_email')
	user_password=request.POST.get('user_password')
	user=authenticate(request,email=user_email, password=user_password)
	print(type(user))
	if user is not None:
		login(request, user)
		return render(request,"userlogin.html")
	else:
		return redirect('login')