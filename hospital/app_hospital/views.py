from django.http import request
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

#sighn-up page render

def sighn(request):
    return render(request,'sighnup.html')

#contact page render

def contact(request):
    return render(request,'contactus.html')
