from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/sighn/',views.sighn,name='sighn'),
    path('contact',views.contact,name='contact'),
    path('accounts/login',views.login,name='login'),
    path('accounts/signup/',views.signup_req, name='signup'),
    
]
