from django.db import models
from django.contrib.auth.models import AbstractUser

class customuser(AbstractUser):
    usertype=[
        ('jobseeker','Job Seeker'),
        ('jobrecruiter','Job Recruiter'),
    ]
    usertype=models.CharField(choices=usertype,max_length=100,null=True)
    FullName=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    PhoneNumber=models.CharField(max_length=50,null=True)
    
    CareerObject=models.CharField(max_length=50,null=True)
    Picture=models.ImageField(upload_to='picture')
    
    
    
    
class resume(models.Model):
    FullName=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    PhoneNumber=models.CharField(max_length=50,null=True)
    EmailAddress=models.CharField(max_length=50,null=True)
    CareerObject=models.CharField(max_length=50,null=True)
    Picture=models.ImageField(upload_to='picture')
    
    # Education
    Degree=models.CharField(max_length=50,null=True)
    Institution=models.CharField(max_length=50,null=True)
    GraduationYear=models.CharField(max_length=50,null=True)
    
    # Work
    Company=models.CharField(max_length=50,null=True)
    Position=models.CharField(max_length=50,null=True)
    StartDate=models.CharField(max_length=50,null=True)
    EndDate=models.CharField(max_length=50,null=True)
    
    # Skill
    HardSkill=models.CharField(max_length=50,null=True)
    SoftSkill=models.CharField(max_length=50,null=True)
    
    Certifications=models.CharField(max_length=50,null=True)
    Projects=models.CharField(max_length=50,null=True)
    References=models.CharField(max_length=50,null=True)
    created_by=models.ForeignKey(customuser,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.FullName
    
class recruiterprofile(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,null=True)
    company=models.CharField(max_length=100,null=True)