from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
 
class Car(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Used', 'Used'),
    )
    TYPE_CHOICES = (
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Sports', 'Sports'),
        ('Convertible', 'Convertible'),
    )
    BRAND_CHOICES = (
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Honda', 'Honda'),
        ('Land-Rover', 'Land-Rover'),
        ('Mercedes', 'Mercedes'),
        ('Toyota', 'Toyota'),
    )
    ENGINE_CHOICES = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
    )
    TRANSMISSION_CHOICES = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    engine = models.CharField(max_length=20, choices=ENGINE_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return self.model


class order(models.Model):
    O_ID = models.IntegerField(primary_key = True)
    Car_ID = models.ForeignKey(Car, default='1', on_delete=models.CASCADE)
    id = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    Date_time = models.DateTimeField()
    Status = models.CharField(max_length=30)
    
class rentcars(models.Model):
    TYPE_CHOICES = (
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Sports', 'Sports'),
        ('Convertible', 'Convertible'),
    )
    BRAND_CHOICES = (
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Honda', 'Honda'),
        ('Land-Rover', 'Land-Rover'),
        ('Mercedes', 'Mercedes'),
        ('Toyota', 'Toyota'),
    )
    ENGINE_CHOICES = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
    )


    Car_ID = models.IntegerField(primary_key = True)
    Type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    Brand = models.CharField(max_length=30, choices=BRAND_CHOICES)
    Model = models.CharField(max_length=30)
    Engine = models.CharField(max_length=30, choices=ENGINE_CHOICES)
    picture = models.ImageField()
    fare = models.CharField(max_length=20)


class rental(models.Model):
    R_ID = models.IntegerField(primary_key = True)
    Car_ID = models.ForeignKey(Car, default='1', on_delete=models.CASCADE)
    id = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    Date_time = models.DateTimeField()
    Rent_hour = models.CharField(max_length=30)
    Rent_fare = models.CharField(max_length=30)

class payment(models.Model):
    P_ID = models.IntegerField(primary_key = True)
    Car_ID = models.ForeignKey(Car, default='1', on_delete=models.CASCADE)
    id = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    transaction_id=models.CharField(max_length=30)
    transaction_amount=models.CharField(max_length=30)
    Date_time = models.DateTimeField()
    Status = models.CharField(max_length=30)
