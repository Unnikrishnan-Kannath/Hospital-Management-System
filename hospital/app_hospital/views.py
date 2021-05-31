from django.http import request
from django.shortcuts import render

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