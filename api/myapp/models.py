from django.db import models

# Create your models here.
class Company(models.Model):
    company_name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(
        ('information technology','IT'),
        ('non information technolgy','Non IT')
    ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.company_name

class Employee(models.Model):
    employee_name=models.CharField(max_length=100)
    email=models.EmailField()
    address= models.CharField(max_length=200)
    phone=models.IntegerField()
    about=models.TextField()
    position=models.CharField(max_length=100,choices=(
        ('manager','manager'),
        ('software developer','software developer'),
        ('Project leader','Project leader')
    ))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name

