from django.db import models

class studentModel(models.Model):
    name=models.CharField(max_length=100)
    roll=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.name +"-"+ self.department + "-" + self.roll