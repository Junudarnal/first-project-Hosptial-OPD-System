from email.policy import default
from django.db import models
from doctor.models import Doctor
from user.constants import STATUS_CHOICES, DEPARTMENTS, GENDER_CHOICES
from user.models import User 


# Create your models here.


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointment', blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_appointment', blank=True, null=True)
    appointment_date=models.DateField()
    appointment_time= models.TimeField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES , default="Pending")
    department=models.CharField(max_length=40,choices=DEPARTMENTS , default="Cardiologist")
    medical_report = models.ImageField(upload_to = 'medical_reports', default="abc.png")
    Prescription = models.ImageField(upload_to = 'prescription', default="abc.png")
    assign_to = models.IntegerField(default = 0)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES, default=" ") 
    address =models.CharField(max_length= 15,default=" ")
    


# class History(models.Model):



