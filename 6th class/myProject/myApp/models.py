from django.db import models


class firstcls(models.Model):
    Name=models.CharField(max_length=70)
    Roll=models.CharField(max_length=70)
    City=models.CharField(max_length=70)
    
    def __str__(self):
        return self.Name
    
class Secondcls(models.Model):
    Film=models.CharField(max_length=70)
    Actor=models.CharField(max_length=70)
    Director=models.CharField(max_length=70)
    
    def __str__(self):
        return self.Film + "-" + self.Actor
    
class thirdcls(models.Model):
    Movie=models.CharField(max_length=40)
    Release_Year=models.CharField(max_length=40)
    Box_office=models.CharField(max_length=40)
    
    def __str__(self):
        return self.Movie + "_" + self.Release_Year
    
class trachermodel(models.Model):
    Name=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name
    
class studentmodel(models.Model):
    Name=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name