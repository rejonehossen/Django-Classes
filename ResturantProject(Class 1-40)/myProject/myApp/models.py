from django.db import models
from django.contrib.auth.models import AbstractUser

class customuser(AbstractUser):
    usertype=[
        ('chef','Chef'),
        ('viewer','Viewer'),
    ]
    gender=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    gender=models.CharField(choices=gender,max_length=100)
    usertype=models.CharField(choices=usertype,max_length=100)
    age=models.IntegerField(null=True)
    city=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100)

class addrecipe(models.Model):
    difficulty_level=[
        ('easy','Easy'),
        ('medium','Medium'),
        ('hard','Hard'),
    ]
    recipe_category=[
        ('breakfast','Breakfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
    ]
    tags=[
        ('vegetarian','Vegetarian'),
        ('non_vegetarian','Non_Vegetarian'),
    ]
    recipe_title=models.CharField(max_length=100,null=True)
    ingredients=models.CharField(max_length=100,null=True)
    instructions=models.TextField(max_length=100,null=True)
    preparation_time=models.CharField(max_length=100,null=True)
    cooking_time=models.CharField(max_length=100,null=True)
    total_time=models.CharField(max_length=100,null=True)
    
    difficulty_level=models.CharField(choices=difficulty_level,max_length=100,null=True)
    
    nutritional_information=models.CharField(max_length=100,null=True)
    sample_recipe_image=models.ImageField(upload_to='static/image/recipe',null=True)
    
    recipe_category=models.CharField(choices=recipe_category,max_length=100,null=True)
    
    tags=models.CharField(choices=tags,max_length=100,null=True)
    
    total_calory=models.CharField(max_length=100,null=True)
    
    created_by=models.ForeignKey(customuser,on_delete=models.CASCADE,null=True)

class basicinformation(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,null=True,related_name='BasicInformation')
    profile_picture=models.ImageField(upload_to='static/image/user')
    full_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    
class chefprofile(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,related_name='ChefProfile')
    
    # Work Experience
    company=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    start=models.CharField(max_length=100)
    end=models.CharField(max_length=100)
    
    # Skill
    hard_skill=models.CharField(max_length=100)
    soft_skill=models.CharField(max_length=100)
    
    certification=models.CharField(max_length=100)
    
class viewerprofile(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,related_name='ViewerProfile')
    interested_food=models.CharField(max_length=100)
    