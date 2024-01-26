
from django import forms
from site import USER_BASE
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from user.models import User,Profile
from .constants import *
from django.contrib.auth.models import Group


class NewUserForm(UserCreationForm):
    email= forms.EmailField(required= True)

    class Meta:
        model = User
        fields = ("first_name","last_name","email","password1","password2")

    def save(self, commit = True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        group = Group.objects.get(name="Patient")
        print(user)
        print(group)

        if commit:
            user.save()
            user.groups.add(group)
        
        return user

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','address','gender']