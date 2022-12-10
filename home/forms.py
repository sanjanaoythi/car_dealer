from django.contrib.auth.forms import forms
#from home.models import Customer
#from home.models import order
#from home.models import payment
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','email','password1','password2']




"""
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'C_ID',
            'C_IMG',
            'Address',
            'NID',
            'u_id',

        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = [
            'O_ID',
            'Car_ID',
            'Cus_ID',
            'Date_time',
            'Status',
            'Address',

        ]

class PaymentForm(forms.ModelForm):
    class Meta:
        model = payment
        fields = [
            'Pa_ID',
            'Pa_type',
            'Pa_check',
            'O_ID',

        ]
"""