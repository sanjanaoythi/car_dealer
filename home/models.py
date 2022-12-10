from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from cars.models import cars

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
    Cus_ID = models.ForeignKey(Customer, default='1', on_delete=models.CASCADE)
    Date_time = models.DateTimeField()
    Status = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
   

class payment(models.Model):
    Pa_ID = models.IntegerField(primary_key = True)
    Pa_type = models.CharField(max_length=30)
    Pa_check = models.CharField(max_length=30)
    O_ID = models.ForeignKey(order, default='1', on_delete=models.CASCADE)