from django.shortcuts import render,redirect
from myApp.models import *

def signup(request):
    
    if request.method=='POST':
        user_name=request.POST.get('user_name')
        display_name=request.POST.get('display_name')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        address=request.POST.get('address')
        date_of_birth=request.POST.get('date_of_birth')
        blood_group=request.POST.get('blood_group')
        gender=request.POST.get('gender')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        email=request.POST.get('email')
        Image=request.FILES.get('Image')
        usertype=request.POST.get('user_type')
        
        if password==confirm_password:
            
            user=customuser.objects.create_user(username=user_name,password=password)
            user.display_name=display_name
            user.email=email
            user.usertype=usertype
            user.first_name=first_name
            user.last_name=last_name
            user.date_of_birth=date_of_birth
            user.address=address
            user.blood_group=blood_group
            user.gender=gender
            user.Image=Image
            user.save()
            return redirect("signin")
        
        else:
            return redirect("signup")
    return render(request,'signup.html')



def signin(request):
    return render(request,'signin.html')