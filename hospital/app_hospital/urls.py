from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path("signup/",views.register,name="reg"),
    path("user_login/",views.user_login,name="user_login"),
    path('accounts/login/login',views.user_login),
    path('signup/login',views.user_login),
    path('accounts/login/user_login',views.user_login),
    
]
