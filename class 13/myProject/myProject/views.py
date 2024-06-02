from django.shortcuts import render, redirect
from myApp.models import *

def index(request):
    return render(request,'index.html')


def studentss(request):
    students=student.objects.all()
    myDict={
        'mod':students
    }
    
    return render(request,'student.html',myDict)

def teacher(request):
    teachers=teachermodel.objects.all()
    myDict={
        'mod':teachers
    }
    return render(request,'teacher.html',myDict)





def addstudent(request):
    
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        dep=request.POST.get('department')
        city=request.POST.get('city')
        
        students=student(
            
            FirstName=fname,
            LastName=lname,
            Department=dep,
            City=city,
            
        )
        students.save()
        return redirect("studentss")
    
    return render(request,'addstudent.html')


def addteacher(request):
    
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        dep=request.POST.get('department')
        city=request.POST.get('city')
        
        teacher=teachermodel(
            FirstName=fname,
            LastName=lname,
            Department=dep,
            City=city,
        )
        teacher.save()
        return redirect("teacher")
    
    return render(request,'addteacher.html')





def deletestudent(request,myid):
    students=student.objects.get(id=myid)
    students.delete()
    
    return redirect("studentss")

def editstudent(request,myid):
    students=student.objects.filter(id=myid)
    myDict={
        'mod':students
    }
    
    return render(request,'editstudent.html',myDict)


def updatestudent(request):
    if request.method=='POST':
        myid=request.POST.get('studentid')
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        dep=request.POST.get('department')
        city=request.POST.get('city')
        
        students=student(
            id=myid,
            FirstName=fname,
            LastName=lname,
            Department=dep,
            City=city,
            
        )
        students.save()
        return redirect("studentss")
    
    



def deleteteacher(request,myid):
    teacher=teachermodel.objects.get(id=myid)
    teacher.delete()
    return redirect("teacher")



def edittreacher(request,myid):
    teacher=teachermodel.objects.filter(id=myid)
    myDict={
        'mod':teacher
    }
    return render(request,'editteacher.html',myDict)


def updateteacher(request):
    
    if request.method=='POST':
        myid=request.POST.get('teacherid')
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        dep=request.POST.get('department')
        city=request.POST.get('city')
        
        teacher=teachermodel(
            id=myid,
            FirstName=fname,
            LastName=lname,
            Department=dep,
            City=city,
        )
        teacher.save()
        
        return redirect("teacher")
    
def viewteacher(request,myid):
    teacher=teachermodel.objects.filter(id=myid)
    myDict={
        'mod':teacher
    }
    return render(request,'viewteacher.html',myDict)


def viewstudent(request,myid):
    std=student.objects.filter(id=myid)
    myDict={
        'mod':std
    }
    
    return render(request,'viewstudent.html',myDict)