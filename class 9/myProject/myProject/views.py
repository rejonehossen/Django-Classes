from django.shortcuts import render, redirect, HttpResponse
from myApp.models import *

def index(request):
    return render(request,'index.html')

def home(request):
    student=studentmodel.objects.all()
    myDict={
        'mod':student
    }
    return render(request,'Home.html',myDict)

def about(request):
    return render(request,'about.html')

def news(request):
    return render(request,'news.html')

def addstudentpage(request):
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        student=studentmodel(
            FirstName=fname,
            LastName=lname,
            Department=department,
            City=city,
        )
        student.save()
        return redirect("home")
    
    return render(request,'addstudentpage.html')

def doctortable(request):
    dct=doctormodel.objects.all()
    myDict={
        'mod':dct
    }
    return render (request,'doctortable.html',myDict)

def teachertable(request):
    tcr=teachermodel.objects.all()
    myDict={
        'mod':tcr
    }
    return render (request,'teachertable.html',myDict)

def table4(request):
    tbl=table4model.objects.all()
    myDict={
        'mod':tbl
    }
    return render (request,'table4.html',myDict)

def table5(request):
    tbl=table5model.objects.all()
    myDict={
        'mod':tbl
    }
    return render (request,'table5.html',myDict)

def doctorform(request):
     if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        age=request.POST.get('age')
        city=request.POST.get('city')
        
        dct=doctormodel(
            FirstName=fname,
            LastName=lname,
            Age=age,
            City=city,
        )
        dct.save()
        return redirect("doctortable")
    
     return render(request,'doctorform.html')



def teacherform(request):
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        student=teachermodel(
            FirstName=fname,
            LastName=lname,
            Department=department,
            City=city,
        )
        student.save()
        return redirect("teachertable")
    return render(request,'teacherform.html')


def table4form(request):
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        student=table4model(
            FirstName=fname,
            LastName=lname,
            Department=department,
            City=city,
        )
        student.save()
        return redirect("table4")
    return render(request,'table4form.html')

def table5form(request):
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        student=table5model(
            FirstName=fname,
            LastName=lname,
            Department=department,
            City=city,
        )
        student.save()
        return redirect("table5")
    return render(request,'table5form.html')




