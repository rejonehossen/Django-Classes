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
        PhoneNumber=request.POST.get('PhoneNumber')
        EmailAddress=request.POST.get('EmailAddress')
        CareerObject=request.POST.get('CareerObject')
        Picture=request.FILES.get('Picture')
        
        Degree=request.POST.get('Degree')
        Institution=request.POST.get('Institution')
        GraduationYear=request.POST.get('GraduationYear')
        
        Company=request.POST.get('Company')
        Position=request.POST.get('Position')
        StartDate=request.POST.get('StartDate')
        EndDate=request.POST.get('EndDate')
        
        HardSkill=request.POST.get('HardSkill')
        SoftSkill=request.POST.get('SoftSkill')
        
        Certifications=request.POST.get('Certifications')
        Projects=request.POST.get('Projects')
        References=request.POST.get('References')
        
        ad=resume(
            FullName=FullName,
            Address=Address,
            PhoneNumber=PhoneNumber,
            EmailAddress=EmailAddress,
            CareerObject=CareerObject,
            Degree=Degree,
            Institution=Institution,
            GraduationYear=GraduationYear,
            Company=Company,
            Position=Position,
            StartDate=StartDate,
            EndDate=EndDate,
            HardSkill=HardSkill,
            SoftSkill=SoftSkill,
            Certifications=Certifications,
            Projects=Projects,
            References=References,
            Picture=Picture,
        )
        ad.save()
        return redirect("data")
    return render(request,'add.html')
    

def deletedata(request,myid):
    dele=resume.objects.get(id=myid)
    dele.delete()
    return redirect("data")

def edit(request,myid):
    edi=resume.objects.filter(id=myid)
    myDict={
        'mod':edi
    }
    return render(request,'edit.html',myDict)


def update(request):
    if request.method=='POST':
        id=request.POST.get('id')
        FullName=request.POST.get('FullName')
        Address=request.POST.get('Address')
        PhoneNumber=request.POST.get('PhoneNumber')
        EmailAddress=request.POST.get('EmailAddress')
        CareerObject=request.POST.get('CareerObject')
        Pictur=request.FILES.get('Picture')
        
        Degree=request.POST.get('Degree')
        Institution=request.POST.get('Institution')
        GraduationYear=request.POST.get('GraduationYear')
        
        Company=request.POST.get('Company')
        Position=request.POST.get('Position')
        StartDate=request.POST.get('StartDate')
        EndDate=request.POST.get('EndDate')
        
        HardSkill=request.POST.get('HardSkill')
        SoftSkill=request.POST.get('SoftSkill')
        
        Certifications=request.POST.get('Certifications')
        Projects=request.POST.get('Projects')
        References=request.POST.get('References')
        
        edt=resume(
            id=id,
            FullName=FullName,
            Address=Address,
            PhoneNumber=PhoneNumber,
            EmailAddress=EmailAddress,
            CareerObject=CareerObject,
            
            Degree=Degree,
            Institution=Institution,
            GraduationYear=GraduationYear,
            Company=Company,
            Position=Position,
            StartDate=StartDate,
            EndDate=EndDate,
            HardSkill=HardSkill,
            SoftSkill=SoftSkill,
            Certifications=Certifications,
            Projects=Projects,
            References=References,
            
            
        )
        if Pictur:
            print(Pictur)
            edt.Picture=Pictur
            
        
        edt.save()
        return redirect("data")
        



def view(request,myid):
    vi=resume.objects.filter(id=myid)
    myDict={
        'mod':vi
    }
    return render(request,'view.html',myDict)











