from django.db import models



class Teachermodel(models.Model):
    FirstName=models.CharField(max_length=100,null=True)
    LastName=models.CharField(max_length=100,null=True)
    TeacherImage=models.ImageField(upload_to="media/Teacher_image",null=True)
    Department=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.FirstName
    
    
    
    
    
    
    
    
class studentmodel(models.Model):
    FirstName=models.CharField(max_length=100,null=True)
    LastName=models.CharField(max_length=100,null=True)
    StdImage=models.ImageField(upload_to="meadia/student_image",null=True)
    Department=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.FirstName
    
    
    
    
class Doctormodel(models.Model):
    FirstName=models.CharField(max_length=100,null=True)
    LastName=models.CharField(max_length=100,null=True)
    DocImage=models.ImageField(upload_to="meadia/doctor_image",null=True)
    Department=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.FirstName