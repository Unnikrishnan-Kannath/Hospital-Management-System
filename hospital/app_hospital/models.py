from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class doctor(models.Model):
    name=models.CharField(max_length=200)
    specialisation=models.CharField(max_length=200)
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone=models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self):
	    return self.name

class user(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    age=models.IntegerField()
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class patient(models.Model):
    unique_id=models.CharField(max_length=10,
    blank=True,
    editable=False,
    unique=True,)
    full_name=models.CharField(max_length=200)
    doctor=models.CharField(max_length=200)
    booking_date=models.DateField()
    age=models.IntegerField()
    mob_num=models.IntegerField()
    address=models.CharField(max_length=200)
    symptoms=models.CharField(max_length=200)
    def __str__(self):
	    return self.full_name

class prescription(models.Model):
    unique_id=models.IntegerField()
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    doctor=models.CharField(max_length=200)
    medicine=models.CharField(max_length=200)
    def __str__(self):
	    return self.name

class pharmacy(models.Model):
    user_name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self):
	    return self.user_name

class register_table(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    
	def _str_(self):
		return self.user.username