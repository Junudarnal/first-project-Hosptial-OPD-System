
from wsgiref.util import application_uri

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from doctor.models import Doctor
from patient.models import Appointment
from user.forms import LoginForm, ProfileUpdateForm
from user.models import User
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from user.decorators import role_required
from patient.models import Appointment
from user.models import Profile
from django.contrib import messages

User = get_user_model()

# Create your views here.
def doctor_login(request):
  if request.method == "POST":
    form = LoginForm(request.POST)
    print("sdhsdfjs")

    print('valid')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email)
    print(password)
    user = authenticate(username=email, password=password)
    print(user)
    if user is not None:
      if user.groups.filter(name="Doctor"):
        login(request, user)
        messages.success(request,"Succesfully login!!")
        return redirect("/doctor/doctor_dashboard/")
      else:
          messages.error(request,"Invalid Group!!")
          return redirect("/doctor/doctor_login/")
    else:
      messages.error(request,"Invalid credential")
      return redirect("/doctor/doctor_login/")

  else:
    #   messages.info(request,"hii")
      form = LoginForm()
      return render(request,"doctor/doctorlogin.html",{'form': form})

@login_required
@role_required(allowed_roles = ['Doctor'],redirect_route="/")
def doctor_dashboard(request):
    
    doctor = Doctor.objects.get(user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor).count()
    profile = Profile.objects.get(user=request.user)

    print(doctor.full_name)
    template_name ='doctor/doctordash.html'
    context = { 'name': 'doctor','doctor':doctor,'ac':appointments,'profile':profile}
    return render(request,template_name,context)

@login_required
@role_required(allowed_roles = ['Doctor'],redirect_route="/")
def doctor_patientappointlist(request):
  doctor = Doctor.objects.get(user = request.user)
  print(doctor.full_name)
  appointlist = Appointment.objects.all().filter(assign_to=doctor.id)
  print(request.user.id)
  print(appointlist)
  appointments = []
  for appointment in appointlist:
    if appointment.status == "Approved":
      appointments.append(appointment) 
  return render(request, 'doctor/patient_appointlist.html',{'appointments':appointments})

@login_required
@role_required(allowed_roles = ['Doctor'],redirect_route="/")
def checkpatient_postnote(request, pk):
  appointment = Appointment.objects.get(id=pk)
  appointment.status = "Checked"
  appointment.save()
  return redirect('/doctor/doctor_patientappointlist/')

@login_required
@role_required(allowed_roles = ['Doctor'],redirect_route="/") 
def checkpatient_status(request):
  appointments = Appointment.objects.filter(status = "Checked")
  print(appointments)
  return render(request,"doctor/checkpatient_postnote.html",{"appointments":appointments})

@login_required
@role_required(allowed_roles = ['Doctor'],redirect_route="/")
def post_prescription(request,pk):
  if request.method == "POST":
    post_prescription = request.FILES.get('Prescription') 
    print(post_prescription)
    appointment = Appointment.objects.get(id=pk)
    appointment.Prescription = post_prescription
    appointment.status = "Finished"
    print(appointment.status)
    appointment.save()
    return redirect('/doctor/checkpatient_status/')

@login_required
@role_required(allowed_roles = ['Doctor'],redirect_route="/") 
def user_logout(request):
  logout(request)
  return redirect('home')

@login_required
@role_required(allowed_roles = ['Doctor'],redirect_route="/")
def update_doctor(request):
 
  if request.method == "POST":
    print("here")
    profileupdateform = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
    # userupdateform = UserUpdateForm(request.POST)
   
    print("profileformnotvalid: ", profileupdateform.is_valid())
    # print("userformnotvalid: ", userupdateform.is_valid())
    if profileupdateform.is_valid():
      profile = profileupdateform.save(commit=False)
      # user = User.objects.get(id = id)
      # profile.user = user
      profile.save()
      return redirect('doctor_dashboard')
    else:
      return HttpResponse("Not Valid")