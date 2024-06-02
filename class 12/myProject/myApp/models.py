from django.db import models



class studentmodel(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Age=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=50)
    
    
    
class Teachermodel(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Age=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=50)