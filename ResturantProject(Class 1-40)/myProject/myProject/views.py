from django.shortcuts import render, redirect
from myApp.models import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages



message={
    'login_success':'successfully Logged In',
    'login_fail_pass_not':'Incorrect username or password. Please enter correct',
    'pas_not_match':'Password and Confirm Password did not matched',
    'New_pass_not_match':'New Password and Confirm New Password did not matched',
    'edit_profile_success':'Profile Updated Successfull',
    'add_recipe_success':'Your recipe successfully added to list',
    'edit_recipe_success':'Your recipe update successfull',
    'Delete_recipe_success':'Recipe deleted successfull',
}
def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        city=request.POST.get('city')
        country=request.POST.get('country')
        usertype=request.POST.get('usertype')
        gender=request.POST.get('gender')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password == confirm_password:
            user=customuser.objects.create_user(username=username,password=password)
            
            for i in first_name:
                if i <= 'z' and i>='a' or i>= "A" and i<= "Z":
                    user.first_name=first_name
                else:
                    messages.warning(request,'First Name cannot be user special charecter or number')
                    return redirect("signup")
            
            user.last_name=last_name
            user.email=email
            user.phone=phone
            user.age=age
            user.city=city
            user.country=country
            user.usertype=usertype
            user.gender=gender
            
            basicinformation.objects.create(myuser=user)
            if usertype == 'chef':
                chefprofile.objects.create(myuser=user)
            elif usertype == 'viewer':
                viewerprofile.objects.create(myuser=user)
            user.save()
            messages.success(request,'Account create successfull')
            return redirect("signin")
        else:
            messages.warning(request,message['pas_not_match'])
            return redirect("signup")
        
    return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,message['login_success'])
            return redirect("hero")
        else:
            messages.warning(request,message['login_fail_pass_not'])
            return redirect("signin")
    return render(request,'signin.html')


def signout(request):
    logout(request)
    messages.success(request,'Log out successfull')
    return redirect("hero")


@login_required
def index(request):
    return render(request,'index.html')
@login_required
def main(request):
    return render(request,'main.html')

def hero(request):
    return render(request,'hero.html')





# Profile

@login_required
def profile(request):
    return render(request,'profile/profile.html')

@login_required
def editprofile(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        city=request.POST.get('city')
        country=request.POST.get('country')
        gender=request.POST.get('gender')
        
        # Basic Informations
        profile_picture=request.POST.get('profile_picture')
        new_profile_picture=request.FILES.get('new_profile_picture')
        full_name=request.POST.get('full_name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        # End Basic Informations
        
        # chefprofile
        # Work Experience 
        company=request.POST.get('company')
        position=request.POST.get('position')
        start=request.POST.get('start')
        end=request.POST.get('end')
        # End Work Experience 
        
        # Skills
        hard_skill=request.POST.get('hard_skill')
        soft_skill=request.POST.get('soft_skill')
        
        # End chefprofile
        
        # viewerprofile
        interested_food=request.POST.get('interested_food')
        # End viewerprofile
        
        
        # Password Section
        password=request.POST.get('password')
        
        if check_password(password,request.user.password):
            request.user.first_name=first_name
            request.user.last_name=last_name
            request.user.email=email
            request.user.age=age
            request.user.city=city
            request.user.country=country
            request.user.gender=gender
            
            # Basic Informations
            if new_profile_picture:
                request.user.BasicInformation.profile_picture=new_profile_picture
            else:
                request.user.BasicInformation.profile_picture=profile_picture
            request.user.BasicInformation.full_name=full_name
            request.user.BasicInformation.address=address
            request.user.BasicInformation.phone=phone
            
            request.user.BasicInformation.save()
            # End Basic Informations
            
            # Chef profile
            if request.user.usertype == 'chef':
                request.user.ChefProfile.company=company
                request.user.ChefProfile.position=position
                request.user.ChefProfile.start=start
                request.user.ChefProfile.end=end
                
                request.user.ChefProfile.hard_skill=hard_skill
                request.user.ChefProfile.soft_skill=soft_skill
                
                request.user.ChefProfile.save()
                
            elif request.user.usertype == 'viewer':
                request.user.ViewerProfile.interested_food=interested_food
                
                request.user.ViewerProfile.save()
                
            request.user.save()
            messages.success(request,message['edit_profile_success'])
            return redirect("profile")
        
        else:
            messages.warning(request,'Incorrect Password')
            return redirect("editprofile")
        
        
    return render(request,'profile/editprofile.html')
@login_required
def changepassword(request):
    if request.method == 'POST':
        current_password=request.POST.get('current_password')
        new_password=request.POST.get('new_password')
        confirm_new_password=request.POST.get('confirm_new_password')
        
        if check_password(current_password,request.user.password):
            if new_password == confirm_new_password:
                request.user.set_password(new_password)
                update_session_auth_hash(request,request.user)
                request.user.save()
                messages.success(request,'Password Changed Successfull')
            else:
                messages.warning(request,message['New_pass_not_match'])
                return redirect("changepassword")
        else:
            messages.warning(request,'Wrong current password. Please try again')
            return redirect("changepassword")
        
    return render(request,'profile/changepassword.html')





@login_required
def addrecipepage(request):
    if request.method == 'POST':
        recipe_title=request.POST.get('recipe_title')
        ingredients=request.POST.get('ingredients')
        instructions=request.POST.get('instructions')
        preparation_time=request.POST.get('preparation_time')
        cooking_time=request.POST.get('cooking_time')
        total_time=request.POST.get('total_time')
        difficulty_level=request.POST.get('difficulty_level')
        nutritional_information=request.POST.get('nutritional_information')
        sample_recipe_image=request.FILES.get('sample_recipe_image')
        recipe_category=request.POST.get('recipe_category')
        tags=request.POST.get('tags')
        total_calory=request.POST.get('total_calory')
        current_user=request.user
        recipe=addrecipe(
            recipe_title=recipe_title,
            ingredients=ingredients,
            instructions=instructions,
            preparation_time=preparation_time,
            cooking_time=cooking_time,
            total_time=total_time,
            difficulty_level=difficulty_level,
            nutritional_information=nutritional_information,
            sample_recipe_image=sample_recipe_image,
            recipe_category=recipe_category,
            tags=tags,
            total_calory=total_calory,
            created_by=current_user,
        )
        recipe.save()
        messages.success(request,message['add_recipe_success'])
        return redirect("recipelist")
    return render(request,'recipe/addrecipe.html')

@login_required
def editrecipe(request,myid):
    current_user=request.user
    recipe=addrecipe.objects.get(id=myid,created_by=current_user)
    myDict={
        'recipe':recipe
    }
    if request.method == 'POST':
        id=request.POST.get('id')
        recipe_title=request.POST.get('recipe_title')
        ingredients=request.POST.get('ingredients')
        instructions=request.POST.get('instructions')
        preparation_time=request.POST.get('preparation_time')
        cooking_time=request.POST.get('cooking_time')
        total_time=request.POST.get('total_time')
        difficulty_level=request.POST.get('difficulty_level')
        nutritional_information=request.POST.get('nutritional_information')
        sample_recipe_image=request.POST.get('sample_recipe_image')
        new_image=request.FILES.get('new_image')
        recipe_category=request.POST.get('recipe_category')
        tags=request.POST.get('tags')
        total_calory=request.POST.get('total_calory')
        current_user=request.user
        recipe=addrecipe(
            id=id,
            recipe_title=recipe_title,
            ingredients=ingredients,
            instructions=instructions,
            preparation_time=preparation_time,
            cooking_time=cooking_time,
            total_time=total_time,
            difficulty_level=difficulty_level,
            nutritional_information=nutritional_information,
            recipe_category=recipe_category,
            
                
            tags=tags,
            total_calory=total_calory,
            created_by=current_user,
        )
        if new_image:
                recipe.sample_recipe_image=new_image
        else:   
                recipe.sample_recipe_image=sample_recipe_image
        recipe.save()
        messages.success(request,message['edit_recipe_success'])
        return redirect("recipelist")
    return render(request,'recipe/editrecipe.html',myDict)

@login_required
def deleterecipe(request,myid):
    current_user=request.user
    recipe=addrecipe.objects.get(id=myid,created_by=current_user)
    recipe.delete()
    messages.success(request,message['Delete_recipe_success'])
    return redirect("recipelist")

@login_required
def recipelist(request):
    current_user=request.user
    recipe=addrecipe.objects.filter(created_by=current_user)
    myDict={
        'recipe':recipe
    }
    return render(request,'recipe/recipelist.html',myDict)

@login_required
def detailsrecipe(request,myid):
    recipe=addrecipe.objects.get(id=myid)
    myDict={
        'recipe':recipe
    }
    return render(request,'recipe/detailsrecipe.html',myDict)