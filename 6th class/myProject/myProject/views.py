from django.shortcuts import render, redirect, HttpResponse
from myApp.models import *


def index(request):
    return render(request,'index.html')

def home(request):
    student=firstcls.objects.all()
    
    myDict={
        'std':student
    }
    return render(request,'home.html',myDict)

def table(request):
    student=Secondcls.objects.all()
    
    myDict={
        'std':student
    }
    
    return render(request,'table.html',myDict)

def student(request):
    modl=studentmodel.objects.all()
    myDict={
        'mod':modl
        
    }
    
    return render(request,'studentmodel.html',myDict)
def teacher(request):
    modl=trachermodel.objects.all()
    myDict={
        'mod':modl
    }
    return render(request,'trachermodel.html',myDict)

def third(request):
    modl=thirdcls.objects.all()
    myDict={
        'mod':modl
    }
    
    return render(request,'thirdcls.html',myDict)