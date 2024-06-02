from django.db import models

class resume(models.Model):
    FullName=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    Picture=models.ImageField(upload_to='pic',null=True)
    PhoneNumber=models.CharField(max_length=50,null=True)
    Email=models.CharField(max_length=50,null=True)
    CareerObject=models.CharField(max_length=50,null=True)
    
    # Education
    Degree=models.CharField(max_length=50,null=True)
    Institution=models.CharField(max_length=50,null=True)
    GraduationYear=models.CharField(max_length=50,null=True)
    
    # Work Experience
    Company=models.CharField(max_length=50,null=True)
    Position=models.CharField(max_length=50,null=True)
    StartDate=models.CharField(max_length=50,null=True)
    EndDate=models.CharField(max_length=50,null=True)
    
    # Skills
    HardSkills=models.CharField(max_length=50,null=True)
    SoftSkill=models.CharField(max_length=50,null=True)
    
    Certification=models.CharField(max_length=50,null=True)
    Projects=models.CharField(max_length=50,null=True)
    References=models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.FullName
