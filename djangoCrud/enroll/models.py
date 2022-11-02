from django.db import models

# Create your models here.
# class User(models.Model):
#     name = models.CharField( max_length=100)
#     designation = models.CharField( max_length=100)
#     email = models.EmailField(max_length=200 ,null=True) 
#     experience = models.IntegerField()

class Employee(models.Model):
    Emp_ID = models.IntegerField( null=True)
    name = models.CharField( max_length=100)
    designation = models.CharField( max_length=100)
    email = models.EmailField(max_length=200 ,null=True) 
    experience = models.CharField(max_length=50)