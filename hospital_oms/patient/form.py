from django.contrib.auth.forms import UserCreationForm
from user.models import *
from patient.models import Appointment
from django import forms


class UserRegisterForm(UserCreationForm):

    # email = forms.EmailField()
    
    # class Meta:
    #     model = User
    #     fields = ['first_name','last_name','username', 'email', 'password', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class BookAppointment(forms.ModelForm):
    # doctorId=forms.ModelChoiceField(queryset=models.doctor.objects.all().filter(status=True),empty_label="Department", to_field_name="user_id")
    class Meta:
        model = Appointment
        fields=['appointment_date','appointment_time','department']

    def save(self, commit=True):
        appointment = super().save(commit=False)

        if commit:
            appointment.save()
        return appointment

# class PatientHistory(forms.ModelForm):
    
#     class Meta:
#         model = History
#         fields=['description','status']
