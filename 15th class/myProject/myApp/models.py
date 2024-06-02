from django.db import models



class teachermodel(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='teacher_pic')
    PDF=models.FileField(upload_to='teacherpdf',null=True)
    
    
    def __str__(self):
        return self.FirstName
    
    
    

class studentmodel(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='student_pic')
    
    
    def __str__(self):
        return self.FirstName