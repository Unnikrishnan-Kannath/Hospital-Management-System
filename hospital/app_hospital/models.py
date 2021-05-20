from django.db import models

# Create your models here.
class doctor(models.Model):
    name=models.CharField(max_length=200)
    specialisation=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class user(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    mob_num=models.IntegerField()
    age=models.IntegerField()
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class patient(models.Model):
    unique_id=models.IntegerField()
    full_name=models.CharField(max_length=200)
    doctor=models.CharField(max_length=200)
    booking_date=models.DateField()
    age=models.IntegerField()
    mob_num=models.IntegerField()
    address=models.CharField(max_length=200)
    symptoms=models.CharField(max_length=200)
    prescription=models.CharField(max_length=200)

class pharmacy(models.Model):
    user_name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)