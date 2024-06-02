from django.shortcuts import render, redirect
from myApp.models import *

def index(request):
    return render(request,'index.html')

def studentdata(request):
    student=studentmodel.objects.all()
    myDict={
        'mod':student
    }
    return render(request,'studentdata.html',myDict)


def addstudent(request):
    if request.method=='POST':
        fname=