from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.user_login, name= 'user_login'),
   path('register/',views.register, name="registeruser"),
   path('logout/', views.user_logout, name="logout"),
   path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
   path('manage_doctor/',views.manage_doctor,name='manage_doctors'),
   path('add_doctor/',views.add_doctor,name='add_doctor'),
   path('manage_patient/',views.manage_patient,name='manage_patients'),
   path('patient_appointlist/',views.patient_appointlist,name='patient_appointlist'),
   path('approve_appointment/',views.approve_appointment,name="approve_appointment"),
   path('reject_appointment/<int:pk>/',views.reject_appointment,name="reject_appointment"),
   path('appoint_history/',views.appoint_history,name="appoint_history"),
   path('delete_patient/<int:pk>',views.delete_patient,name="delete_patient"),
   path('delete_doctor/<int:pk>',views.delete_doctor,name="delete_doctor"),
   path('edit_doctor/<int:pk>',views.edit_doctor,name="edit_doctor"),
   path('update_admin/',views.update_admin,name="update_admin")
]
  

