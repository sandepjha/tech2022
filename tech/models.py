from tkinter import CASCADE
from django.db import models

# Create your models here.

class Profile(models.Model):
    Name = models.CharField(max_length=30)
    DOB = models.DateField()
    Gender = models.CharField(max_length=10)
    Phone = models.IntegerField()
    Owner = models.ForeignKey('Profile', on_delete=models.CASCADE)
    Address1 = models.CharField(max_length=50)
    Address2 = models.CharField(max_length=50)
    Pincode = models.IntegerField()

