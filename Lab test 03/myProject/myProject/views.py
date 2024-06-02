from django.shortcuts import *
from myApp.models import *

def index(request):
    return render(request,'index.html')


def data(request):
    var=resume.objects.all()
    myDict={
        'mod':var
    }
    return render(request,'data.html',myDict)

def add(request):
    if request.method=='POST':
        FullName=request.POST.get('FullName')
        Address=request.POST.get('Address')
        PhoneNumber=request.POST.get('PhoneNumber')
        Email=request.POST.get('Email')
        ProfilePicture=request.FILES.get('ProfilePicture')
        CareerObject=request.POST.get('CareerObject')
        
        Degree=request.POST.get('Degree')
        Instituiton=request.POST.get('Instituiton')
        GraduationYear=request.POST.get('GraduationYear')
        
        Company=request.POST.get('Company')
        Position=request.POST.get('Position')
        StartDate=request.POST.get('StartDate')
        EndDate=request.POST.get('EndDate')
        
        HardSkills=request.POST.get('HardSkills')
        SoftSkills=request.POST.get('SoftSkills')
        
        Certifications=request.POST.get('Certifications')
        Projects=request.POST.get('Projects')
        Reference=request.POST.get('Reference')
        var=resume(
            FullName=FullName,
            Address=Address,
            PhoneNumber=PhoneNumber,
            Email=Email,
            ProfilePicture=ProfilePicture,
            CareerObject=CareerObject,
            
            Degree=Degree,
            Instituiton=Instituiton,
            GraduationYear=GraduationYear,
            
            Company=Company,
            Position=Position,
            StartDate=StartDate,
            EndDate=EndDate,
            
            HardSkills=HardSkills,
            SoftSkills=SoftSkills,
            
            Certifications=Certifications,
            Projects=Projects,
            Reference=Reference,
        )
        var.save()
        return redirect("data")
    return render(request,'add.html')

def delete(request,myid):
    var=resume.objects.get(id=myid)
    var.delete()
    return redirect("data")

def edit(request,myid):
    var=resume.objects.filter(id=myid)
    myDict={
        'mod':var
    }
    return render(request,'edit.html',myDict)

def update(request):
    if request.method=='POST':
        id=request.POST.get('id')
        FullName=request.POST.get('FullName')
        Address=request.POST.get('Address')
        PhoneNumber=request.POST.get('PhoneNumber')
        Email=request.POST.get('Email')
        ProfilePicture=request.FILES.get('ProfilePicture')
        CareerObject=request.POST.get('CareerObject')
        
        Degree=request.POST.get('Degree')
        Instituiton=request.POST.get('Instituiton')
        GraduationYear=request.POST.get('GraduationYear')
        
        Company=request.POST.get('Company')
        Position=request.POST.get('Position')
        StartDate=request.POST.get('StartDate')
        EndDate=request.POST.get('EndDate')
        
        HardSkills=request.POST.get('HardSkills')
        SoftSkills=request.POST.get('SoftSkills')
        
        Certifications=request.POST.get('Certifications')
        Projects=request.POST.get('Projects')
        Reference=request.POST.get('Reference')
        var=resume(
            id=id,
            FullName=FullName,
            Address=Address,
            PhoneNumber=PhoneNumber,
            Email=Email,
            
            CareerObject=CareerObject,
            
            Degree=Degree,
            Instituiton=Instituiton,
            GraduationYear=GraduationYear,
            
            Company=Company,
            Position=Position,
            StartDate=StartDate,
            EndDate=EndDate,
            
            HardSkills=HardSkills,
            SoftSkills=SoftSkills,
            
            Certifications=Certifications,
            Projects=Projects,
            Reference=Reference,
            ProfilePicture=ProfilePicture,
        )
        if ProfilePicture:
            print(ProfilePicture)
            
        var.save()    
        return redirect("data")
    


def view(request,myid):
    var=resume.objects.filter(id=myid)
    myDict={
        'resume':var
    }
    return render(request,'view.html',myDict)