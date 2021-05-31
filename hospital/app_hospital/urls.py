from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('sighn',views.sighn,name='sighn'),
    path('contact',views.contact,name='contact')
    
]
