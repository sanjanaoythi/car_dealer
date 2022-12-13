from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from cars.models import cars
from django.contrib.auth.forms import UserCreationForm 
from django import forms
# Create your models here.
 
class Customer(models.Model):
    C_ID = models.IntegerField(primary_key = True)
    C_IMG = models.ImageField()
    Address = models.CharField(max_length=30)
    NID = models.IntegerField()
    u_id = models.ForeignKey(User, default='1', on_delete=models.CASCADE)


class order(models.Model):
    O_ID = models.IntegerField(primary_key = True)
    Car_ID = models.ForeignKey(cars, default='1', on_delete=models.CASCADE)
    id = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    Date_time = models.DateTimeField()
    Status = models.CharField(max_length=30)
    
   

class payment(models.Model):
    Pa_ID = models.IntegerField(primary_key = True)
    Pa_type = models.CharField(max_length=30)
    Pa_check = models.CharField(max_length=30)
    O_ID = models.ForeignKey(order, default='1', on_delete=models.CASCADE)



    class UserCreateForm(UserCreationForm):
         email = forms.EmailField(required=True,label='Email',error_messages={'exists': 'This Already Exists'})

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    #placeholder
    def _init_(self, *args, **kwargs):
        super(UserCreateForm, self)._init_(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'



    def save(self, commit=True):            # defalt commit value true
        user = super(UserCreateForm, self).save(commit=False)
        '''it will return to the obj but not save in database.useful for custom process'''
        user.email = self.cleaned_data['email']  # valid or not
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']