
from django.db import models

# Create your models here.

class Vehicle(models.Model):
    name = models.CharField(max_length=64)
    status = models.CharField(max_length=64 , choices= [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('InShop', 'InShop'),
    ])
    condition = models.CharField(max_length=64 , choices= [
        ('Good', 'Good'),
        ('Satisfactory' , 'Satisfactory'),
        ('Critical', 'Critical'),
    ])

    # def __str__(self):
    #     return self.name

class Consum(models.Model):
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    consumption = models.IntegerField(default=0)
    date = models.DateField()

    # def __str__(self) -> str:
    #     return self.vehicle_id
