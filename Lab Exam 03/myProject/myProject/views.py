from django.shortcuts import render, redirect
from myApp.models import *

def index(request):
    return render(request,'index.html')



def data(request):
    dt=resume.objects.all()
    myDict={
        'mod':dt
    }
    return render(request,'data.html',myDict)



def add(request):
    if request.method=='POST':
        FullName=request.POST.get('FullName')
        Address=request.POST.get('Address')
        Picture=request.FILES.get('Picture')
        PhoneNumber=request.POST.get('PhoneNumber')
        Email=request.POST.get('Email')
        CareerObject=request.POST.get('CareerObject')
        Degree=request.POST.get('Degree')
        Institution=request.POST.get('Institution')
        GraduationYear=request.POST.get('GraduationYear')
        Position=request.POST.get('Position')
        Company=request.POST.get('Company')
        StartDate=request.POST.get('StartDate')
        EndDate=request.POST.get('EndDate')
        HardSkills=request.POST.get('HardSkills')
        SoftSkill=request.POST.get('SoftSkill')
        Certification=request.POST.get('Certification')
        Projects=request.POST.get('Projects')
        References=request.POST.get('References')
        
        dt=resume(
            FullName=FullName,
            Address=Address,
            Picture=Picture,
            PhoneNumber=PhoneNumber,
            Email=Email,
            CareerObject=CareerObject,
            Institution=Institution,
            Degree=Degree,
            GraduationYear=GraduationYear,
            Position=Position,
            Company=Company,
            StartDate=StartDate,
            EndDate=EndDate,
            HardSkills=HardSkills,
            SoftSkill=SoftSkill,
            Certification=Certification,
            Projects=Projects,
            References=References,
        )
        dt.save()
        return redirect("data")
    return render(request,'add.html')



def delete(request,myid):
    dt=resume.objects.get(id=myid)
    dt.delete()
    return redirect("data")

def edit(request,myid):
    dt=resume.objects.filter(id=myid)
    myDict={
        'mod':dt
    }
    return render(request,'edit.html',myDict)


def update(request):
    if request.method=='POST':
        id=request.POST.get('id')
        FullName=request.POST.get('FullName')
        Address=request.POST.get('Address')
        Picture=request.FILES.get('Picture')
        PhoneNumber=request.POST.get('PhoneNumber')
        Email=request.POST.get('Email')
        CareerObject=request.POST.get('CareerObject')
        Degree=request.POST.get('Degree')
        Institution=request.POST.get('Institution')
        GraduationYear=request.POST.get('GraduationYear')
        Position=request.POST.get('Position')
        Company=request.POST.get('Company')
        StartDate=request.POST.get('StartDate')
        EndDate=request.POST.get('EndDate')
        HardSkills=request.POST.get('HardSkills')
        SoftSkill=request.POST.get('SoftSkill')
        Certification=request.POST.get('Certification')
        Projects=request.POST.get('Projects')
        References=request.POST.get('References')
        
        dt=resume(
            id=id,
            FullName=FullName,
            Address=Address,
            PhoneNumber=PhoneNumber,
            Email=Email,
            CareerObject=CareerObject,
            Institution=Institution,
            Degree=Degree,
            GraduationYear=GraduationYear,
            Position=Position,
            Company=Company,
            StartDate=StartDate,
            EndDate=EndDate,
            HardSkills=HardSkills,
            SoftSkill=SoftSkill,
            Certification=Certification,
            Projects=Projects,
            References=References,
            
        )
        if Picture:
            print(Picture)
            dt.Picture=Picture
            
        dt.save()
        return redirect("data")


def view(request,myid):
    dt=resume.objects.filter(id=myid)
    myDict={
        
        'mod':dt
    }
    return render(request,'view.html',myDict)