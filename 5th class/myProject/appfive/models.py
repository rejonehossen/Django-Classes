from django.db import models

class mone(models.Model):
    one=models.CharField(max_length=50)
    two=models.CharField(max_length=50)
    three=models.CharField(max_length=50)
    
    def __str__(self):
        return self.one
    
class mtwo(models.Model):
    name=models.CharField(max_length=70)
    
    def __str__(self):
        return self.name
    
class mthree(models.Model):
    roll=models.CharField(max_length=70)
    
    def __str__(self):
        return self.roll
    
class mfour(models.Model):
    roll=models.CharField(max_length=50)
    
    def __str__(self):
        return self.roll
    
class modelfive(models.Model):
    roll=models.CharField(max_length=50)
    
    def __str__(self):
        return self.roll