from django.db import models
from django.contrib.auth.models import AbstractUser

class customuser(AbstractUser):
    usertype=[
        ('chef','Chef'),
        ('viewer','viewer'),
        ('owner','Owner'),
    ]
    gender=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    gender=models.CharField(choices=gender,max_length=100,null=True)
    usertype=models.CharField(choices=usertype,max_length=100,null=True)
    Age=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    Country=models.CharField(max_length=100,null=True)
    



class recipemodel(models.Model):
    tags=[
        ('vegetarian','Vegetarian'),
        ('nonvegetarian','Non_Vegetarian'),
    ]
    ctg=[
        ('break_fast','Break_Fast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
    ]
    lv=[
        ('ealy_','Easy_'),
        ('medium_','Medium_'),
        ('hard_','Hard_'),
    ]
    # category=[
    #     ('breakfast'),('BreakFast'),
    #     ('lunch'),('Lunch'),
    #     ('Dinne'),('Dinner'),
    # ]
    # level=[
    #     ('easylevel'),('Easy Level'),
    #     ('mediumlevel'),('MediumLevel'),
    #     ('hardlevel'),('HardLevel'),
    # ]
    RecipeTitle=models.CharField(max_length=100,null=True)
    Ingredients=models.CharField(max_length=100,null=True)
    Instructions=models.CharField(max_length=100,null=True)
    PreparationTime=models.CharField(max_length=100,null=True)
    CookingTime=models.CharField(max_length=100,null=True)
    TotalTime=models.CharField(max_length=100,null=True)
    
    NutritionlaInformation=models.CharField(max_length=100,null=True)
    SampleRecipeImage=models.ImageField(upload_to='static/pic/recipepicture',null=True)
    RecipeCategory=models.CharField(choices=ctg,max_length=100,null=True)
    DifficultyLevel=models.CharField(choices=lv,max_length=100,null=True)
    Tags=models.CharField(choices=tags,max_length=100,null=True)
    TotalCalorie=models.CharField(max_length=100,null=True)
    created_by=models.ForeignKey(customuser,on_delete=models.CASCADE,null=True)
    

class chefprofile(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,null=True)
    experience=models.PositiveIntegerField(null=True)
    skills=models.CharField(max_length=100,null=True)
    resumelatter=models.CharField(max_length=100,null=True)
    profilepicture=models.ImageField(upload_to='static/picture/profile/chef',null=True)
    # own=models.ForeignKey(customuser,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.myuser.username
    

class viewerprofile(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,null=True)
    interest=models.CharField(max_length=100,null=True)
    profilepicture=models.ImageField(upload_to='static/picture/profile/viewer',null=True)
    
    def __str__(self):
        return self.myuser.username