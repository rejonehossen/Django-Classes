from django.db import models

class mapptwo(models.Model):
    name=models.CharField(max_length=100)
    roll=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name +" "+ self.city
    
    
class mtwotwo(models.Model):
    name=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    department=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name +" "+ self.department
    

class mtwothree(models.Model):
    name=models.CharField(max_length=50)
    two=models.IntegerField(max_length=50)
    three=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name +" "+ self.three
    
class mtwofour(models.Model):
    name=models.CharField(max_length=50)
    nametwo=models.CharField(max_length=50)
    namethree=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name +" " + self.nametwo
    
class mtwofive(models.Model):
    name=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    country=models.CharField(max_length=70)
    
    def __str__(self):
        return self.name +" " + self.city