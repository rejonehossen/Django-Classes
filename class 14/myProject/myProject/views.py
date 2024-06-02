from django.shortcuts import render, redirect
from myApp.models import *

def index(request):
    return render(request,'index.html')


def studentss(request):
    students=studentmodel.objects.all()
    myDict={
        'mod':students
    }
    
    return render(request,'student.html',myDict)

def teacher(request):
    teachers=Teachermodel.objects.all()
    myDict={
        'mod':teachers
    }
    return render(request,'teacher.html',myDict)





def addstudent(request):
    
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        stdImage=request.FILES.get('stdImage')
        dep=request.POST.get('department')
        city=request.POST.get('city')
        
        students=studentmodel(
            
            FirstName=fname,
            LastName=lname,
            StdImage=stdImage,
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
        TeacherImage=request.FILES.get('teacherpic')
        dep=request.POST.get('department')
        city=request.POST.get('city')
        
        teacher=Teachermodel(
            FirstName=fname,
            LastName=lname,
            TeacherImage=TeacherImage,
            Department=dep,
            City=city,
        )
        teacher.save()
        return redirect("teacher")
    
    return render(request,'addteacher.html')





def deletestudent(request,myid):
    students=studentmodel.objects.get(id=myid)
    students.delete()
    
    return redirect("studentss")

def editstudent(request,myid):
    students=studentmodel.objects.filter(id=myid)
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
        
        students=studentmodel(
            id=myid,
            FirstName=fname,
            LastName=lname,
            Department=dep,
            City=city,
            
        )
        students.save()
        return redirect("studentss")
    
    



def deleteteacher(request,myid):
    teacher=Teachermodel.objects.get(id=myid)
    teacher.delete()
    return redirect("teacher")



def edittreacher(request,myid):
    teacher=Teachermodel.objects.filter(id=myid)
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
        
        teacher=Teachermodel(
            id=myid,
            FirstName=fname,
            LastName=lname,
            Department=dep,
            City=city,
        )
        teacher.save()
        
        return redirect("teacher")
    
def viewteacher(request,myid):
    teacher=Teachermodel.objects.filter(id=myid)
    myDict={
        'mod':teacher
    }
    return render(request,'viewteacher.html',myDict)


def viewstudent(request,myid):
    std=studentmodel.objects.filter(id=myid)
    myDict={
        'mod':std
    }
    
    return render(request,'viewstudent.html',myDict)

def home(request):
    teacher=Teachermodel.objects.all()
    student=studentmodel.objects.all()
    myDict={
        'mod':teacher,
        'std':student
    }
    return render(request,'home.html',myDict)





def doctor(request):
    doctor=Doctormodel.objects.all()
    myDict={
        'mod':doctor
    }
    return render(request,'doctor.html',myDict)




def adddoctor(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        image=request.FILES.get('image')
        dep=request.POST.get('Department')
        city=request.POST.get('city')
        
        Doctor=Doctormodel(
            FirstName=firstname,
            LastName=lastname,
            DocImage=image,
            Department=dep,
            City=city,
        )
        
        
        Doctor.save()
        return redirect("doctor")
    return render(request,'adddoctor.html')