# # Create your views here.

from telnetlib import STATUS
from django.shortcuts import redirect, render, HttpResponse,get_object_or_404
# from hospital_oms.patient.views import appointment_status
from patient.models import Appointment

from user.forms import NewUserForm, LoginForm, ProfileUpdateForm,UserUpdateForm
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate
from doctor.forms import doctorcreationform
from doctor.models import Doctor
from user.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from user.decorators import role_required
from user.models import Profile
from django.contrib.auth.models import Group





# # # Create your views here.
# def user_login(request):
#     template_name ='user/user.html'
#     context = { 'name': 'users','age':20}
#     return render(request,template_name,context)

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
          form.save()
          messages.success(request, "Registration successful")
          return redirect("login")
        else:
          messages.error(request,"Unsuccessful registration, Invalid information.")
        
    form = NewUserForm()
    return render(request, template_name = 'user/user.html', context = { "register_form": form})

def user_login(request):
  if request.method == "POST":
    print("inside")
    form = LoginForm(request.POST)
    # print(form)
    if form.is_valid():
      print("is valid") 
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      print(username)
      print(password)
      user = authenticate(username = username, password = password)
      print('user', user)
      if user is not None:
        login(request, user)
        group = user.groups.all()
        if group:
          print("gg",  group, group[0])
          if group[0].name == 'Admin':
            # print('here')
            return redirect('/user/admin_dashboard/')
          else:
            messages.info(request,"You are not authorized to login!!!")

          if group[0] == 'Doctor':
               return render(request,"doctor/doctordash.html")
          else:
            messages.info(request,"You are not authorized to login!!!")

          if group[0] == 'Patient':
               return render(request,"patient/patientdash.html")
          else:
            messages.info(request,"You are not authorized to login!!!")
    else:
      messages.info(request,"Invalid!!")
      form = LoginForm()
  else:
    form = LoginForm()
  return render(request,"user/login.html",{'loginform':form})

@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def user_logout(request):
  logout(request)
  return redirect('home')

@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def manage_doctor(request):
  
  users = Doctor.objects.all()

  doctors = []
  for doctor in users:
    if doctor.user.groups.filter(name="Doctor"):
      doctors.append(doctor)
  return render(request,'user/managedoctor.html',{'Doctors':doctors})

@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def admin_dashboard(request):
  profile = Profile.objects.get(user=request.user)
  admin = User.objects.get(username=request.user.username)

  patients = User.objects.filter(groups__name='Patient').count()
  doctors = User.objects.filter(groups__name='Doctor').count()



  appointments = Appointment.objects.all().count()
  updateform = ProfileUpdateForm(instance=profile)
  # userupdateform = UserUpdateForm(instance=admin)
  
  template_name ='user/admindash.html'
  context = { 'name': 'user','profile':profile,'admin':admin,'appoint':appointments,'patient_count':patients,'doctor_count':doctors,"updateform":updateform}
  return render(request,template_name,context)


@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def manage_patient(request):
  users = User.objects.all()
  patients = []

  for patient in users:
    if patient.groups.filter(name="Patient"):
      patients.append(patient)
  return render(request,'user/managepatients.html',{"patients":patients})

@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def add_doctor(request):
  if request.method=='POST':
        full_name=request.POST.get('full_name')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        contact_no = request.POST.get('contact_no')
        department = request.POST.get('department')
        usergroup = Group.objects.get(name="Doctor")
       

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('/user/add_doctor/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('/user/add_doctor/')
            else:
                print("hereeeeee")
                user=User.objects.create(username=username,email=email,first_name=full_name) 
                user.set_password(password1)
                Doctor.objects.create(full_name=full_name,user=user,gender=gender,contact_no=contact_no,department=department,address=address) 
                user.groups.add(usergroup)
                user.save()
                print('User created')
                return redirect('/user/manage_doctor/')
        else:
            messages.info(request,"Password not matching")
            return redirect('/user/add_doctor/')
  return render(request,'user/add_doctor.html')

@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/") 
def patient_appointlist(request):
  appointments = Appointment.objects.exclude(status = "Approved").exclude(status="Rejected")

  doctors = Doctor.objects.all()
  
  return render(request, 'user/patient_appointlist.html',{'appointments':appointments,'doctors':doctors})

@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def approve_appointment(request):
  appid = request.POST.get('appid')
  doctorid = request.POST.get('assigneddoctor')
  appointment = Appointment.objects.get(id=appid)
  appointment.assign_to = doctorid
  appointment.status = "Approved"
  appointment.save()
  return redirect('/user/patient_appointlist/')

@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def update_admin(request):
 
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
      return redirect('admin_dashboard')
    else:
      return HttpResponse("Not Valid")




@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def reject_appointment(request,pk):
  appointment = Appointment.objects.get(id=pk)
  appointment.status = "Rejected"
  appointment.save()
  return redirect('/user/patient_appointlist/')


@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def appoint_history(request):
  appointments = Appointment.objects.all().exclude(status ="Pending")
  appointlist = Appointment.objects.all()
  appointments = []
  for appointment in appointlist:
    if appointment.status == "Approved" or appointment.status == "Rejected":
      appointments.append(appointment) 
  return render(request, 'user/appoint_history.html', {'appointments': appointments})


@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def delete_patient(request, pk):
  patient = User.objects.all().filter(id=pk).delete()
  return redirect('/user/manage_patient/')


@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def delete_doctor(request, pk):
  doctor = Doctor.objects.all().filter(id=pk).delete()
  return redirect('/user/manage_doctor/')


@login_required
@role_required(allowed_roles = ['Admin'],redirect_route="/")
def edit_doctor(request, pk):
    obj = get_object_or_404(Doctor, id=pk)
    if request.method == "POST":
        form = Doctor(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request,"Doctor Updated!!")
            return render(request, '/user/edit_doctor.html/')
    
    form = Doctor(request.GET)
    doctor = Doctor.objects.all()
    return render(request,'user/edit_doctor.html',{"text":'Edit','form':form,'Action':"user/edit_doctor/"+str(id)})