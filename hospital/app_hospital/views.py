from django.http import request
from django.shortcuts import render,redirect
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