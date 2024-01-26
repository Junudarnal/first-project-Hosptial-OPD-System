from django.urls import path
from . import views

urlpatterns = [
   path('patient_register/', views.patient_register, name= 'patient_register'),
   path('patient_login/', views.patient_login, name ='patient_login'),
   path('logout/', views.user_logout, name="logout"),
   path('patient_dashboard/', views.patient_dashboard, name= 'patient_dashboard'),
   path('book_appointment/', views.book_appointment, name= 'book_appointment'),
   path('appointment_status/', views.appointment_status, name= 'appointment_status'),
   path('patient_medical_history/', views.patient_medical_history, name= 'patient_medical_history'),
   path('delete_prescription/<int:pk>',views.delete_prescription,name="delete_prescription"),
    path('update_patient/',views.update_patient,name="update_patient")
   # path('patient_profile/',views.profile,name="patient_profile"),
]