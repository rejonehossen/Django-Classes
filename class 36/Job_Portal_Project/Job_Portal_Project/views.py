from django.shortcuts import render,redirect
from JobApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash

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
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        blood=request.POST.get('blood')
        usertype=request.POST.get('usertype')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        city=request.POST.get('city')
        country=request.POST.get('country')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        profile_photo=request.FILES.get('profile_photo')
        
        if password == confirm_password:
            user=customuser.objects.create_user(username=username,password=password)
            user.age=age
            user.gender=gender
            user.blood=blood
            user.usertype=usertype
            user.first_name=first_name
            user.last_name=last_name
            user.city=city
            user.country=country
            user.profile_photo=profile_photo
            
            if usertype == 'jobrecruiter':
                recruiterprofile.objects.create(myuser=user).save()
                basicinformation.objects.create(myuser=user).save()
                contact.objects.create(myuser=user).save()
            elif usertype == 'jobseeker':
                seekerprofile.objects.create(myuser=user).save()
                basicinformation.objects.create(myuser=user).save()
                contact.objects.create(myuser=user).save()
                educational_qualification.objects.create(myuser=user).save()
                work_experience.objects.create(myuser=user).save()
            
                
            user.save()
            messages.success(request,'account create successfull')
            return redirect("signin")
        else:
            return redirect("signup")
    return render(request,'signup.html')


def signout(request):
    logout(request)
    return redirect("signin")


@login_required
def addjobpage(request):
    if request.method == 'POST':
        job_title=request.POST.get('job_title')
        job_description=request.POST.get('job_description')
        job_location=request.POST.get('job_location')
        deadline=request.POST.get('deadline')
        company_logo=request.FILES.get('company_logo')
        requirements=request.POST.get('requirements')
        qualifications=request.POST.get('qualifications')
        job_types=request.POST.get('job_types')
        workplace=request.POST.get('workplace')
        salary=request.POST.get('salary')
        experience=request.POST.get('experience')
        current_user=request.user
        user=addjob(
            job_title=job_title,
            job_description=job_description,
            job_location=job_location,
            deadline=deadline,
            company_logo=company_logo,
            requirements=requirements,
            qualifications=qualifications,
            job_types=job_types,
            workplace=workplace,
            salary=salary,
            experience=experience,
            created_by=current_user,
        )
        user.save()
        return redirect("joblist")
    return render(request,'addjobpage.html')

@login_required
def editjob(request,myid):
    job=addjob.objects.filter(id=myid)
    myDict={
        'mod':job
    }
    return render(request,'editjob.html',myDict)

def updatejob(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        job_title=request.POST.get('job_title')
        job_description=request.POST.get('job_description')
        job_location=request.POST.get('job_location')
        deadline=request.POST.get('deadline')
        company_logo=request.POST.get('company_logo')
        newimage=request.FILES.get('newimage')
        requirements=request.POST.get('requirements')
        qualifications=request.POST.get('qualifications')
        job_types=request.POST.get('job_types')
        workplace=request.POST.get('workplace')
        salary=request.POST.get('salary')
        experience=request.POST.get('experience')
        current_user=request.user
        user=addjob(
            id=id,
            job_title=job_title,
            job_description=job_description,
            job_location=job_location,
            deadline=deadline,
            
            requirements=requirements,
            qualifications=qualifications,
            job_types=job_types,
            workplace=workplace,
            salary=salary,
            experience=experience,
            created_by=current_user,
        )
        if newimage:
            company_logo=newimage
        else:
            company_logo=company_logo
        user.save()
        return redirect("joblist")




@login_required
def editprofile(request):
    if request.method == 'POST':
        current_user=request.user
        # CUSTOM USER
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        blood=request.POST.get('blood')
        # usertype=request.POST.get('usertype')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        city=request.POST.get('city')
        country=request.POST.get('country')
        # username=request.POST.get('username')
        profile_photo=request.FILES.get('profile_photo')
        
        # END CUSTOM USER
        
        # Recruiter profile
        company_name=request.POST.get('company_name')
        company_location=request.POST.get('company_location')
        recruiter_name=request.POST.get('recruiter_name')
        
        # End Recruiter profile
        
        # Seeker profile
        qualification=request.POST.get('qualification')
        experience=request.POST.get('experience')
        skills=request.POST.get('skills')
        
        # End Seeker profile
        
        # basicinformation
        fathername=request.POST.get('fathername')
        mothername=request.POST.get('mothername')
        address=request.POST.get('address')
        
        # end basicinformation
        
        # contact
        phone=request.POST.get('phone')
        emergnecy_contact=request.POST.get('emergnecy_contact')
        
        
        
        
        
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password == confirm_password:
            if check_password(password, current_user.password):
                current_user.age=age
                current_user.gender=gender
                current_user.blood=blood
                current_user.first_name=first_name
                current_user.last_name=last_name
                current_user.city=city
                current_user.country=country
                
                current_user.BasicInformation.fathername=fathername
                current_user.BasicInformation.mothername=mothername
                current_user.BasicInformation.address=address
                current_user.BasicInformation.save()
                
                current_user.Contact.phone=phone
                current_user.Contact.emergnecy_contact=emergnecy_contact
                current_user.Contact.save()
                
                if current_user.usertype == 'jobrecruiter' :
                # recruiterprofile
                
                    recruiter=current_user.RecruiterProfile
                    recruiter.company_name=company_name
                    recruiter.company_location=company_location
                    recruiter.recruiter_name=recruiter_name
                    recruiter.save()
                    
                # end recruiterprofile
                    
                elif current_user.usertype == 'jobseeker' :
                # seekerprofile
                
                    
                    current_user.SeekerProfile.qualification=qualification
                    current_user.SeekerProfile.experience=experience
                    current_user.SeekerProfile.skills=skills
                    current_user.SeekerProfile.save()

                # End Seekerprofile
                
                
                current_user.save()
                
                return redirect("profile")
        
    return render(request,'editprofile.html')



@login_required
def changepassword(request):
    current_user=request.user
    if request.method == 'POST':
        currentPassword=request.POST.get('currentPassword')
        newPassword=request.POST.get('newPassword')
        confirmPassword=request.POST.get('confirmPassword')
        if check_password(currentPassword,current_user.password):
            if newPassword == confirmPassword:
                current_user.password=newPassword
                current_user.set_password(newPassword)
                current_user.save()
                update_session_auth_hash(request,current_user)
                
                return redirect("profile")
    
    return render(request,'changepassword.html')

@login_required
def index(request):
    return render(request,'index.html')
@login_required
def joblist(request):
    uuser=request.user
    job=addjob.objects.filter(created_by=uuser)
    myDict={
        'mod':job
    }
    return render(request,'joblist.html',myDict)
@login_required
def profile(request):
    # User=request.user
    # if User.usertype == 'jobrecruiter':
    #     profi=customuser.objects.filter()
    # elif User.usertype == 'jobseeker':
    #     profi=customuser.objects.filter()
        
    # myDict={
    #     'profi':profi
    # }
    return render(request,'profile.html')
@login_required
def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def viewjob(request,id):
    
    
    job=addjob.objects.filter(id=id)
    myDict={
        'mod':job
    }
    return render(request,'viewjob.html',myDict)






def basicinformationform(request):
    return render(request,'basicinformationform.html')


def edicationform(request):
    if request.method == 'POST':
        user=request.user
        degree=request.POST.get('degree')
        institution=request.POST.get('institution')
        year=request.POST.get('year')
        cnt=educational_qualification(
            degree=degree,
            institution=institution,
            year=year,
            myuser=user,
        )
        cnt.save()
        return redirect("edicationdata")
    return render(request,'edicationform.html')


def contactform(request):
    
        
    return render(request,'contactform.html')


def workform(request):
    return render(request,'workform.html')







def basicinformationdata(request):
    return render(request,'basicinformationdata.html')



def edicationdata(request):
    return render(request,'edicationdata.html')



def contactdata(request):
    return render(request,'contactdata.html')



def workdata(request):
    return render(request,'workdata.html')



def editeducation(request):
    user=request.user
    edu=educational_qualification.objects.get(myuser=user)
    myDict={
        'mod':edu
    }
    return render(request,'editeducation.html',myDict)


def updateeducation(request):
    if request.method == 'POST':
        user=request.user
        degree=request.POST.get('degree')
        institution=request.POST.get('institution')
        year=request.POST.get('year')
        cnt=educational_qualification(
            degree=degree,
            institution=institution,
            year=year,
            myuser=user,
        )
        cnt.save()
        return redirect("edicationdata")