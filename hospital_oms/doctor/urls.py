from django.urls import path
from . import views

urlpatterns = [
   path('doctor_login/', views.doctor_login, name ='doctor_login'),
   path('logout/', views.user_logout, name="logout"),
   path('doctor_dashboard/', views.doctor_dashboard, name= 'doctor_dashboard'),
   path('doctor_patientappointlist/', views.doctor_patientappointlist, name= 'doctor_patientappointlist'),
   path('checkpatient_postnote/<int:pk>/', views.checkpatient_postnote, name= 'checkpatient_postnote'), 
   path('checkpatient_status/', views.checkpatient_status, name= 'checkpatient_status'),
   path('post_prescription/<int:pk>/', views.post_prescription, name= 'post_prescription'),
   path('update_doctor/',views.update_doctor,name="update_doctor")
   
]
   
