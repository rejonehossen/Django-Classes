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
    

class addjobmodel(models.Model):
    rename=models.CharField(max_length=100,null=True)
    jobtitle=models.CharField(max_length=100,null=True)
    companyname=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    companydescription=models.CharField(max_length=100,null=True)
    jobdescription=models.CharField(max_length=100,null=True)
    qualifications=models.CharField(max_length=100,null=True)
    salaryinformation=models.CharField(max_length=100,null=True)
    deadline=models.CharField(max_length=100,null=True)
    resignation=models.CharField(max_length=100,null=True)
    experience=models.CharField(max_length=100,null=True)
    created_by=models.ForeignKey(customuser,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.jobtitle + "created by" + self.created_by.username
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    