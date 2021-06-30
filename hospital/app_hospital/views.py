#from hospital.app_hospital.models import user
from django.http import request
from django.db import models
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, auth
from .models import pharmacy,register_table,doctor

# Create your views here.
def home(request):
    return render(request,'index.html')

#sighn-up page render

def sighn(request):
    return render(request,'registration/sighnup.html')

#contact page render

def contact(request):
    return render(request,'contactus.html')

def register(request):
	if request.method=="POST":
		fname=request.POST["first_name"]
		last=request.POST["lastname"]
		un=request.POST["username"]
		em=request.POST["email"]
		phn=request.POST["phn"]
		pwd=request.POST["psw"]
		rpwd=request.POST["psw-repeat"]
		tp=request.POST["utype"]

		usr=User.objects.create_user(username=un,email=em,password=pwd)
		usr.first_name=fname
		usr.last_name=last
		if tp=="employee":
			usr.is_staff=True
		usr.save()
		reg=register_table(user=usr,phone_number=phn)
		reg.save()
		return render(request,"registration/login.html",{"status":"{} Register Successfully".format(fname)})

	return render(request,"registration.html")

def user_login(request):
	if request.method=="POST":
		un=request.POST["username"]
		ps=request.POST["password"]
		
		user=authenticate(username=un,password=ps)
		if user:
			login(request,user)
			if user.is_superuser: 
				return redirect("/admin")
			if user.is_staff:
				return redirect("contact")
			if user.is_active:
				return redirect("home")


		else:
			return render(request,'user_login.html',{"status":"Invalid User Name or Password"})

