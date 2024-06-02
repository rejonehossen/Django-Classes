from django.shortcuts import render,redirect
from myApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
    if request.method=='POST':
        user_name=request.POST.get('user_name')
        pass_word=request.POST.get('password')
        
        user=authenticate(username=user_name,password=pass_word)
        
        
        if user:
            login(request,user)
            return redirect("dashboard")
        else:
            return redirect("signin")
    
    
    
    return render(request,'signin.html')


@login_required
def index(request):
    return render(request,'index.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')



@login_required
def viewjob(request):
    
    job=addjobmodel.objects.all()
    myDict={
        'mod':job
    }
    
    return render(request,'viewjob.html',myDict)



@login_required
def addjob(request):
    if request.method == 'POST':
        jobtitle=request.POST.get('jobtitle')
        company_name=request.POST.get('companyname')
        address=request.POST.get('address')
        company_description=request.POST.get('companydescription')
        job_description=request.POST.get('jobdescription')
        qualifications=request.POST.get('qualifications')
        salary=request.POST.get('salary')
        deadline=request.POST.get('deadline')
        resignation=request.POST.get('resignation')
        experience=request.POST.get('experience')
        current_user=request.user
        
        addjob=addjobmodel(
            jobtitle=jobtitle,
            companyname=company_name,
            address=address,
            companydescription=company_description,
            jobdescription=job_description,
            qualifications=qualifications,
            salaryinformation=salary,
            deadline=deadline,
            resignation=resignation,
            experience=experience,
            created_by=current_user,
            # rename=request.user.username
        )
        addjob.save()
        return redirect("viewjob")
        
        
    
    
    return render(request,'job/addjob.html')

@login_required
def viewjob(request):
    
    current_user = request.user
    
    myjob=addjobmodel.objects.filter(created_by=current_user)
    
    myDict={
        'mod':myjob
    }
    
    return render(request,'job/viewjob.html',myDict)

@login_required
def deletejob(request,myid):
    dele=addjobmodel.objects.get(id=myid)
    dele.delete()
    return redirect("viewjob")


@login_required
def detailsjob(request,myid):
    dele=addjobmodel.objects.filter(id=myid)
    myDict={
        'mod':dele
    }
    return render(request,'detailsjob.html',myDict)


@login_required
def editjob(request,myid):
    edi=addjobmodel.objects.filter(id=myid)
    myDict={
        'mod':edi
    }
    return render(request,'editjob.html',myDict)



@login_required
def updatejob(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        jobtitle=request.POST.get('jobtitle')
        company_name=request.POST.get('companyname')
        address=request.POST.get('address')
        company_description=request.POST.get('companydescription')
        job_description=request.POST.get('jobdescription')
        qualifications=request.POST.get('qualifications')
        salary=request.POST.get('salary')
        deadline=request.POST.get('deadline')
        resignation=request.POST.get('resignation')
        experience=request.POST.get('experience')
        current_user=request.user
        
        addjob=addjobmodel(
            jobtitle=jobtitle,
            id=id,
            companyname=company_name,
            address=address,
            companydescription=company_description,
            jobdescription=job_description,
            qualifications=qualifications,
            salaryinformation=salary,
            deadline=deadline,
            resignation=resignation,
            experience=experience,
            created_by=current_user,
        )
        addjob.save()
        return redirect("viewjob")
    
    
    
    
@login_required
def recentjob(request):
    return render(request,'job/jecentjob.html')

@login_required
def appliedjob(request):
    return render(request,'job/appliedjob.html')


@login_required
def profile(request):
    
    return render(request,'profile.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect("signin")

@login_required
def viewjobseeker(request):
    job=addjobmodel.objects.all()
    myDict={
        'mod':job
    }
    return render(request,'job/viewjobseeker.html',myDict)




