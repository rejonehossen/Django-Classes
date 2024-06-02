from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myApp.models import *




def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("dashboard")
        else:
            return redirect("signin")
    return render(request,'signin.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        gender=request.POST.get('gender')
        Age=request.POST.get('age')
        City=request.POST.get('city')
        Country=request.POST.get('country')
        usertype=request.POST.get('usertype')
        if password == confirm_password:
            user=customuser.objects.create_user(username=username, password=password)
            user.email=email
            user.gender=gender
            user.Age=Age
            user.City=City
            user.Country=Country
            user.usertype=usertype
            user.save()
            return redirect("signin")
        else:
            return redirect("sigup")
    return render(request,'signup.html')

@login_required
def signout(request):
    logout(request)
    return redirect("signin")


@login_required
def dashboard(requset):
    return render(requset,'dashboard.html')



@login_required
def profile(request):
    return render(request,'profile.html')




@login_required
def addrecipe(request):
    if request.method == 'POST':
        recipe_title=request.POST.get('recipe_title')
        ingredients=request.POST.get('ingredients')
        instructions=request.POST.get('instructions')
        preparation_time=request.POST.get('preparation_time')
        cooking_time=request.POST.get('cooking_time')
        total_time=request.POST.get('total_time')
        nutritional_information=request.POST.get('nutritional_information')
        sample_recipe_image=request.FILES.get('sample_recipe_image')
        difficulty_level=request.POST.get('difficulty_level')
        tags=request.POST.get('tags')
        recipe_category=request.POST.get('recipe_category')
        
        total_calorie=request.POST.get('total_calorie')
        current_user=request.user
        use=recipemodel(
            RecipeTitle=recipe_title,
            Ingredients=ingredients,
            PreparationTime=preparation_time,
            CookingTime=cooking_time,
            TotalTime=total_time,
            NutritionlaInformation=nutritional_information,
            SampleRecipeImage=sample_recipe_image,
            RecipeCategory=recipe_category,
            DifficultyLevel=difficulty_level,
            Tags=tags,
            TotalCalorie=total_calorie,
            Instructions=instructions,
            created_by=current_user,
            
        )
        use.save()
        return redirect("listrecipe")
    
    
    return render(request,'addrecipe.html')

@login_required
def listrecipe(request):
    current_user=request.user
    
    lst=recipemodel.objects.filter(created_by=current_user)
    myDict={
        'mod':lst
    }
    
    return render(request,'listrecipe.html',myDict)



@login_required
def listrecipeforviewer(request):
    lst=recipemodel.objects.all()
    myDict={
        'mod':lst
    }
    return render(request,'listrecipeforviewer.html',myDict)

@login_required
def viewrecipe(request,myid):
    lst=recipemodel.objects.filter(id=myid)
    myDict={
        'mod':lst
    }
    return render(request,'viewrecipe.html',myDict)


@login_required
def deleterecipe(request,myid):
    dl=recipemodel.objects.get(id=myid)
    dl.delete()
    return redirect("listrecipe")

@login_required
def editrecipe(request,myid):
    reci=recipemodel.objects.filter(id=myid)
    myDict={
        'mod':reci
    }
    return render(request,'editrecipe.html',myDict)

@login_required
def updaterecipe(request):
    if request.method == 'POST':
        
        recipe_title=request.POST.get('recipe_title')
        id=request.POST.get('id')
        ingredients=request.POST.get('ingredients')
        instructions=request.POST.get('instructions')
        preparation_time=request.POST.get('preparation_time')
        cooking_time=request.POST.get('cooking_time')
        total_time=request.POST.get('total_time')
        nutritional_information=request.POST.get('nutritional_information')
        sample_recipe_image=request.FILES.get('sample_recipe_image')
        difficulty_level=request.POST.get('difficulty_level')
        tags=request.POST.get('tags')
        recipe_category=request.POST.get('recipe_category')
        
        total_calorie=request.POST.get('total_calorie')
        current_user=request.user
        use=recipemodel(
            id=id,
            RecipeTitle=recipe_title,
            Ingredients=ingredients,
            PreparationTime=preparation_time,
            CookingTime=cooking_time,
            TotalTime=total_time,
            NutritionlaInformation=nutritional_information,
            SampleRecipeImage=sample_recipe_image,
            RecipeCategory=recipe_category,
            DifficultyLevel=difficulty_level,
            Tags=tags,
            TotalCalorie=total_calorie,
            Instructions=instructions,
            created_by=current_user,
            
        )
        use.save()
        return redirect("listrecipe")
    

# @login_required
# def viewrecipeforfollowers(request)