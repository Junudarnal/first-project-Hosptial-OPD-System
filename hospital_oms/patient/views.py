from email import message
from unicodedata import name
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.decorators import role_required
from patient.models import Appointment
from . import form

# from patient import models
from django.contrib.auth import authenticate
from user.forms import NewUserForm, LoginForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.db import models
from patient import models as p_models
from user.models import Profile


from django.contrib.auth import get_user_model

User = get_user_model()


def patient_login(request):
  if request.method == "POST":
    form = LoginForm(request.POST)
    # print("sdhsdfjs")
    if form.is_valid():
      print('valid')
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      print(user)
      if user is not None:
          group = Group.objects.get(name="Patient")
          if user.groups.filter(name=group):
            login(request,user)
            return redirect("/patient/patient_dashboard")
          else:
            messages.error(request,"Invalid User Group!")
            return redirect("/patient/patient_login/")
      else:
        messages.error(request,"Invalid Credentials")
        return redirect("/patient/patient_login/")

    
    else:
        messages.error(request,"Invalid Form")
        return redirect('patient_login')
        messages.info(request,"form not Invalid")
  else:
      print("The method is get")
    #   messages.info(request,"hii")
      form = LoginForm()
      return render(request,"patient/patientlogin.html",{'form': form})

@login_required
@role_required(allowed_roles = ['Patient'],redirect_route="/")
def patient_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    patient = User.objects.get(username=request.user.username)
    appointments = Appointment.objects.filter(patient=patient).count()
    print(appointments)
    template_name ='patient/patientdash.html'
    context = { 'name': 'patient','profile':profile,'patient':patient,'appointments':appointments}
    return render(request,template_name,context)


def patient_register(request):
    if request.method =='POST':
        first_name= request.POST['Fname']
        last_name= request.POST['Lname']
        username= request.POST['Uname']
        email= request.POST['Email']
        password= request.POST['Pass']
        password2= request.POST['Pass']
        gender= request.POST['gender']
        address=request.POST['address']
        
        if password == password2:
            # print("yeta samma thik chha")
            if User.objects.filter(username = username).exists():
                print('Username taken')
            
            elif User.objects.filter(email= email).exists():
                print('Email taken')
            else:
                user = User.objects.create_user(username = username,password = password, email=email, first_name= first_name, last_name=last_name,
                gender= gender,address=address)
                user.save()
                user.groups.add(Group.objects.get(name='Patient'))
                print('User Created')
                return redirect( 'home')
        else:
            messages.info(request,'password not matching..')
            return redirect('patient_register')
        return redirect('home')
    
    else:
        # print('here')
        return render(request,'patient/patient_register.html')

@login_required
@role_required(allowed_roles = ['Patient'],redirect_route="/")
def patient_logout(request):
  logout(request)
  return redirect('home')


@login_required
@role_required(allowed_roles = ['Patient'],redirect_route="/")
def book_appointment(request):
    message=None
    if request.method=='POST':
        appointmentForm= form.BookAppointment(request.POST,request.FILES)
        if appointmentForm.is_valid():
            print('valid')
            appointment = appointmentForm.save()
            appointment.patient = request.user
            appointment.gender = request.user.gender
            appointment.medical_report = request.FILES.get('medical_report')
            appointment.save()
            return redirect('patient_dashboard')
        print(appointmentForm.errors)
        return HttpResponse("form is not valid")
    appointmentForm= form.BookAppointment()
    mydict={'appointmentForm':appointmentForm,'patient':'g','message':message}

    return render(request,'patient/bookappoint.html',context=mydict)

# def patient_medical_history(request):
#     if request.method == 'POST':

@login_required
@role_required(allowed_roles = ['Patient'],redirect_route="/")
def appointment_status(request):
    patient = request.user
    print(patient)

    appointments=p_models.Appointment.objects.filter(patient = patient).filter()
    print(appointments)

    return render(request,"patient/appointstatus.html",{"appointments":appointments})

@login_required
@role_required(allowed_roles = ['Patient'],redirect_route="/")
def patient_medical_history(request):
    appointment = Appointment.objects.filter(status = "Finished")
    return render(request, 'patient/patienthistory.html',{"appointment": appointment})

@login_required
@role_required(allowed_roles = ['Patient'],redirect_route="/")
def delete_prescription(request, pk):
  prescription = Appointment.objects.all().filter(id=pk).delete()
  return redirect('/patient/patient_medical_history/')

@login_required
@role_required(allowed_roles = ['Patient'],redirect_route="/")
def user_logout(request):
  logout(request)
  return redirect('home')

# def profile(request):
#     if request.user.is_authenticated:
#         return render(request, '/patient/patientprofile.html/')
#     else:
#         return redirect('home')
@login_required
@role_required(allowed_roles = ['Patient'],redirect_route="/")
def update_patient(request):
 
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
      return redirect('patient_dashboard')
    else:
      return HttpResponse("Not Valid")