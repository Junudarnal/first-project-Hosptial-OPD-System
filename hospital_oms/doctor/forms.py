from dataclasses import fields
from pydoc import doc
from tkinter import Widget
from django import forms
from site import USER_BASE
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from user.models import *
from user.constants import *
from django.contrib.auth.models import Group
from user.constants import *
from doctor.models import Doctor
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email= forms.EmailField(required= True)

    class Meta:
        model = User
        fields = ("first_name","last_name","email","password1","password2")

    def save(self, commit = True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        group = Group.objects.get(name="Doctor")
        print(user)
        print(group)

        if commit:
            user.save()
            user.groups.add(group)
        return user


class doctorcreationform(forms.ModelForm):
    class meta:
        model = Doctor
        fields = ('full_name','contact_no','gender','department')

    # full_name = forms.CharField(max_length=100)
    # contact_no = forms.IntegerField(max_value=15)
    # gender = forms.ChoiceField(choices=GENDER_CHOICES)
    # department = forms.ChoiceField(choices=DEPARTMENTS)
