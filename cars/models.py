from django.db import models

# Create your models here.

class cars(models.Model):
    Car_ID = models.IntegerField(primary_key = True)
    Type = models.CharField(max_length=30)
    Brand = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    Engine = models.CharField(max_length=30)
    picture = models.ImageField()
    Price = models.FloatField()
    