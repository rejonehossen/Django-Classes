from django.db import models
from django.contrib.auth.models import AbstractUser


class customuser(AbstractUser):
    usertype=[
        ('jobrecruiter','jobrecruiter'),
        ('jobseeker','jobseeker'),
        ('viewer','viewer'),
    ]
    gender=[
        ('male','male'),
        ('female','female'),
        ('other','other'),
    ]
    blood=[
        ('a','a'),
        ('ab','ab'),
        ('b','b'),
        ('o','o'),
    ]
    age=models.CharField(max_length=100,null=True)
    
    gender=models.CharField(choices=gender,max_length=100,null=True)
    blood=models.CharField(choices=blood,max_length=100,null=True)
    usertype=models.CharField(choices=usertype,max_length=100,null=True)
    
    city=models.CharField(max_length=100,null=True)
    
    country=models.CharField(max_length=100,null=True)
    profile_photo=models.ImageField(upload_to='profilephoto')



class addjob(models.Model):
    jobtype=[
        ('fulltime','full_time'),
        ('parttime','part_time'),
    ]
    workplace=[
        ('remote','remote'),
        ('onsite','on_site'),
    ]
    job_title=models.CharField(max_length=100,null=True)
    job_description=models.CharField(max_length=100,null=True)
    job_location=models.CharField(max_length=100,null=True)
    deadline=models.CharField(max_length=100,null=True)
    company_logo=models.ImageField(upload_to='jobpic',null=True)
    requirements=models.CharField(max_length=100,null=True)
    qualifications=models.CharField(max_length=100,null=True)
    
    job_types=models.CharField(choices=jobtype,max_length=100,null=True)
    
    workplace=models.CharField(choices=workplace,max_length=100,null=True)
    salary=models.CharField(max_length=100,null=True)
    experience=models.CharField(max_length=100,null=True)
    created_by=models.ForeignKey(customuser,on_delete=models.CASCADE,null=True)


class recruiterprofile(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,null=True, related_name='RecruiterProfile')
    company_name=models.CharField(max_length=100,null=True)
    company_location=models.CharField(max_length=100,null=True)
    recruiter_name=models.CharField(max_length=100,null=True)


class seekerprofile(models.Model):
    lasteducation=[
        ('ssc','SSC'),
        ('hsc','HSC'),
        ('honours','Honours'),
    ]
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,null=True, related_name='SeekerProfile')
    qualification=models.CharField(max_length=100,null=True)
    experience=models.CharField(max_length=100,null=True)
    skills=models.CharField(max_length=100,null=True)
    lasteducation=models.CharField(choices=lasteducation,max_length=100,null=True)
    
class basicinformation(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,related_name='BasicInformation')
    fathername=models.CharField(max_length=100,null=True)
    mothername=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)


class contact(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,related_name='Contact')
    
    phone=models.CharField(max_length=100)
    emergnecy_contact=models.CharField(max_length=100)
    
    
    
class educational_qualification(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,related_name='Educational_Qualification')
    degree=models.CharField(max_length=100)
    institution=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    
    
class work_experience(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,related_name='Work_Experience')
    
    company_name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    start=models.CharField(max_length=100)
    end=models.CharField(max_length=100)
    