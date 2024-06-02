from django.db import models


class studentmodel(models.Model):
    FirstName=models.CharField(max_length=50,null=True)
    LastName=models.CharField(max_length=50,null=True)
    Department=models.CharField(max_length=90,null=True)
    City=models.CharField(max_length=90,null=True)
    
    def __str__(self):
        return self.FirstName

class doctormodel(models.Model):
    FirstName=models.CharField(max_length=50,null=True)
    LastName=models.CharField(max_length=50,null=True)
    Age=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.FirstName
    
class teachermodel(models.Model):
    FirstName=models.CharField(max_length=50,null=True)
    LastName=models.CharField(max_length=50,null=True)
    Department=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.FirstName
    

class table4model(models.Model):
    FirstName=models.CharField(max_length=50,null=True)
    LastName=models.CharField(max_length=50,null=True)
    Department=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.FirstName
    
    
    
class table5model(models.Model):
    FirstName=models.CharField(max_length=50,null=True)
    LastName=models.CharField(max_length=50,null=True)
    Department=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.FirstName