from django.shortcuts import render,redirect
from myApp.models import *

def index(request):
    return render(request,'index.html')


def teacherdata(request):
    teacher=teachermodel.objects.all()
    myDict={
        'mod':teacher
    }
    return render(request,'teacherdata.html',myDict)

def addteacher(request):
    if request.method=='POST':
        FirstName=request.POST.get('FirstName')
        LastName=request.POST.get('LastName')
        Age=request.POST.get('Age')
        City=request.POST.get('City')
        Image=request.FILES.get('Image')
        
        
        teacher=teachermodel(
            FirstName=FirstName,
            LastName=LastName,
            Age=Age,
            City=City,
            Image=Image,
            
            
            
        )
        teacher.save()
        return redirect("teacherdata")
    return render(request,'addteacher.html')


def deleteteacher(request,myid):
    teacher=teachermodel.objects.get(id=myid)
    teacher.delete()
    return redirect("teacherdata")


def editteacher(request,myid):
    teacher=teachermodel.objects.filter(id=myid)
    myDict={
        'mod':teacher
    }
    
    return render(request,'editteacher.html',myDict)



def updateteacher(request):
    if request.method=='POST':
        id=request.POST.get('id')
        FirstName=request.POST.get('FirstName')
        LastName=request.POST.get('LastName')
        Age=request.POST.get('Age')
        City=request.POST.get('City')
        Image=request.FILES.get('Image')
        
        teacher=teachermodel(
            id=id,
            FirstName=FirstName,
            LastName=LastName,
            Age=Age,
            City=City,
            
            
            
        )
        if Image:
            print(Image)
            teacher.Image=Image
        teacher.save()
        return redirect("teacherdata")
    
    
    
    
def viewteacher(request,myid):
    teacher=teachermodel.objects.filter(id=myid)
    myDict={
        'mod':teacher
    }
    return render(request,'viewteacher.html',myDict)



