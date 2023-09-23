

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Car

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'  # Include all fields from the Car model