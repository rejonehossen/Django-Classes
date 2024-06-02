from django.db import models

from django.contrib.auth.models import AbstractUser

class customuser(AbstractUser):
    usertype=[
        ('requiter','Requiter'),('jobseeker','Jobseeker')
    ]
    gender=[
        ('male','Male'),('female','Female'),('other','Other')
    ]
    blood=[
        ('a+','A+'),('b+','B+'),('o+','O+'),('ab+','AB+'),('a-','A-'),('b-','B-'),('o-','O-'),('ab-','AB-')
    ]
    
    display_name=models.CharField(max_length=100,null=True)
    Image=models.ImageField(upload_to='picture',null=True)
    address=models.CharField(max_length=100,null=True)
    date_of_birth=models.CharField(max_length=100,null=True)
    usertype=models.CharField(choices=usertype,max_length=100,null=True)
    gender=models.CharField(choices=gender,max_length=100,null=True)
    blood_group=models.CharField(choices=blood,max_length=100,null=True)
    
