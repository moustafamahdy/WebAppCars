from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from rest_framework import serializers

# Create your models here.
class Staff(models.Model):
    StaffID = models.IntegerField(null=False, primary_key=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    PhoneNo = models.IntegerField(null=False)
    
    
    def __str__(self):
        return f"{self.StaffID}: {self.first_name} {self.last_name}"


class Car(models.Model):
    CarNo = models.IntegerField( null=False, primary_key=True)
    CarName = models.CharField(max_length=30, null=False)
    CarModel = models.IntegerField( null=False)
    staff = models.ForeignKey(Staff, on_delete=CASCADE, related_name="carstaff")
    

    def __str__(self):
        return f"{self.CarNo}: {self.CarName} ({self.CarModel})"

class Customer(models.Model):
    CustomerID = models.IntegerField( null=False, primary_key=True)
    PassportNo = models.CharField(max_length=15, null=False)
    FirstName = models.CharField(max_length=20, null=False)
    LastName = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=30, null=False)
    phone = models.IntegerField(null=False)


    def __str__(self):
        return f"{self.CustomerID}: {self.FirstName} {self.LastName} "

class Rental(models.Model):
    RentalNO = models.IntegerField(null=False, primary_key=True)
    CarNo = models.ForeignKey(Car, on_delete=CASCADE, null=False)
    StaffID = models.ForeignKey(Staff, on_delete=CASCADE)
    CustomerId = models.ForeignKey(Customer, on_delete=CASCADE)
    Timeout = models.DateField(null=False)
    TimeReturn = models.DateField(null=False)

    def __str__(self):
        return f"{self.RentalNO}: {self.CustomerId} from {self.Timeout} to {self.TimeReturn}"




