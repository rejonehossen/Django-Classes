from django.db import models

class one(models.Model):
    ONE=models.CharField(max_length=50)
    two=models.CharField(max_length=50)
    three=models.CharField(max_length=50)
    
    def __str__(self):
        return self.ONE + " " + self.three
    
class two(models.Model):
    one=models.CharField(max_length=40)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    
    def __str__(self):
        return self.city + " " + self.one
    
class three(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + " " + self.city
    
class four(models.Model):
    name=models.CharField(max_length=70)
    roll=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    
    def __str__(self):
        return self.name + " " + self.roll
    
    
class five(models.Model):
    name=models.CharField(max_length=70)
    roll=models.CharField(max_length=70)
    department=models.CharField(max_length=70)
    
    def __str__(self):
        return self.name + " " + self.roll