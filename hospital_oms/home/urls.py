from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name ='home'),
    path('home/about/', views.about, name="about"),
    path('home/contactinfo/', views.contactinfo, name="contactinfo"),
    # path('signup', views.handleSignUp, name="handleSignUp"),
]
