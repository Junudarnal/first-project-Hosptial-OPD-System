from django.db import models
from user.constants import DEPARTMENTS
from user.models import User

# Create your models here.
class Doctor(models.Model):
    department = models.CharField(max_length=50, choices=DEPARTMENTS, default='Cardiologist')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50,default="")
    gender=models.CharField(max_length=6, default="")
    contact_no=models.PositiveIntegerField(blank=True, null=True)
    address =models.CharField(max_length=50,default="")
    