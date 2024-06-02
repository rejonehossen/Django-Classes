from django.db import models

class one(models.Model):
    name=models.CharField(max_length=70)
    roll=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    
    def __str__(self):
        return self.name + " " + self.roll
    
class two(models.Model):
    name=models.CharField(max_length=50)
    roll=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class three(models.Model):
    name=models.CharField(max_length=50)
    country=models.CharField(max_length=40)
    city=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name + " " + self.city
    
class four(models.Model):
    one=models.CharField(max_length=70)
    two=models.CharField(max_length=70)
    threerow=models.CharField(max_length=70)
    
    def __str__(self):
        return self.two
    
class five(models.Model):
    nam=models.CharField(max_length=40)
    namtwo=models.CharField(max_length=50)
    namthree=models.CharField(max_length=70)
    
    def __str__(self):
        return self.nam + " " + self.namtwo