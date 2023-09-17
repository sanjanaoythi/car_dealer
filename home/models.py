from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
 
class cars(models.Model):
    Car_ID = models.IntegerField(primary_key = True)
    Type = models.CharField(max_length=30)
    Brand = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    Engine = models.CharField(max_length=30)
    picture = models.ImageField()
    Price = models.CharField(max_length=10)


class order(models.Model):
    O_ID = models.IntegerField(primary_key = True)
    Car_ID = models.ForeignKey(cars, default='1', on_delete=models.CASCADE)
    id = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    Date_time = models.DateTimeField()
    Status = models.CharField(max_length=30)
    
class rentcars(models.Model):
    Car_ID = models.IntegerField(primary_key = True)
    Type = models.CharField(max_length=30)
    Brand = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    Engine = models.CharField(max_length=30)
    picture = models.ImageField()
    fare = models.CharField(max_length=20)


class rental(models.Model):
    R_ID = models.IntegerField(primary_key = True)
    Car_ID = models.ForeignKey(cars, default='1', on_delete=models.CASCADE)
    id = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    Date_time = models.DateTimeField()
    Rent_hour = models.CharField(max_length=30)
    Rent_fare = models.CharField(max_length=30)

class payment(models.Model):
    P_ID = models.IntegerField(primary_key = True)
    Car_ID = models.ForeignKey(cars, default='1', on_delete=models.CASCADE)
    id = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    transaction_id=models.CharField(max_length=30)
    transaction_amount=models.CharField(max_length=30)
    Date_time = models.DateTimeField()
    Status = models.CharField(max_length=30)