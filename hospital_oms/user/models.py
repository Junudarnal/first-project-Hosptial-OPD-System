import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

from .constants import GENDER_CHOICES

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES, default="Male")   
    address = models.CharField(max_length=50,default="") 
    # Fname =models.CharField(max_length=25, default=0)
    # Lname =models.CharField(max_length=25, default=0)
    # Uname = models.CharField(max_length=100, unique=True)
    # number = models.PositiveIntegerField( default=0)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to="profile/",default="profile/icon.jpg" )


    def __str__(self) -> str:
        return f'{self.user}'
