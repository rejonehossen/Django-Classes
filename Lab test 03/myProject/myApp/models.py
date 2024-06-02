from django.db import models

class resume(models.Model):
    FullName=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    PhoneNumber=models.CharField(max_length=50,null=True)
    Email=models.CharField(max_length=50,null=True)
    ProfilePicture=models.ImageField(upload_to='profile_picture',null=True)
    CareerObject=models.TextField()
    
    # Education
    Degree=models.CharField(max_length=50,null=True)
    Instituiton=models.CharField(max_length=50,null=True)
    GraduationYear=models.CharField(max_length=50,null=True)
    
    # Work Experience
    Company=models.CharField(max_length=50,null=True)
    Position=models.CharField(max_length=50,null=True)
    StartDate=models.CharField(max_length=50,null=True)
    EndDate=models.CharField(max_length=50,null=True)
    
    # Skills
    HardSkills=models.CharField(max_length=50,null=True)
    SoftSkills=models.CharField(max_length=50,null=True)
    
    Certifications=models.CharField(max_length=50,null=True)
    Projects=models.CharField(max_length=50,null=True)
    Reference=models.CharField(max_length=50,null=True)
