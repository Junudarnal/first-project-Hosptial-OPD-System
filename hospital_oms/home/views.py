from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.contrib.auth.models import User 

# Create your views here.
def display(request):
    template_name ='home/home.html'
    context = { 'name': 'home'}
    return render(request,template_name,context)

def about(request):
    template_name ='home/about.html'
    context = { 'name': 'about'}
    return render(request,template_name,context)

def contactinfo(request):
    template_name ='home/contact.html'
    context = { 'name': 'contactinfo'}
    return render(request,template_name,context)

# def contact(request):
#     if request.method=="POST":
#         name=request.POST['name']
#         email=request.POST['email']
#         phone=request.POST['phone']
#         content =request.POST['content']
    #     if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
    #         messages.error(request, "Please fill the form correctly")
    #     else:
    #         contact=Contact(name=name, email=email, phone=phone, content=content)
    #         contact.save()
    #         messages.success(request, "Your message has been successfully sent")
    # return render(request, "home/contact.html")

# def handleSignUp(request):
#     if request.method=="POST":
#         # Get the post parameters
#         username=request.POST['username']
#         email=request.POST['email']
#         fname=request.POST['fname']
#         lname=request.POST['lname']
#         pass1=request.POST['pass1']
#         pass2=request.POST['pass2']

#         # check for errorneous input
        
#         # Create the user
#         user = User.objects.create_user(username, email, pass1)
#         user.first_name= fname
#         user.last_name= lname
#         user.save()
#         messages.success(request, " Your iCoder has been successfully created")
#         return redirect('home')

#     else:
#         return HttpResponse("404 - Not found")


