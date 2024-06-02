from django.shortcuts import render, redirect, HttpResponse

def homepage(request):
    veriable01={
        'name':'Abdullah Al Mamun',
        'department':'CSE',
        'City':'Kushtia',
        'name02':'Rejone',
        'department02':'English',
        'city02':'Narayangonj',
    }
    return render(request,'homepage.html',veriable01)

def no2(request):
    return render(request,'Second.html')







def no3(request):
    
    myDict={
        'Name':'Rejone',
        'Department':'ICT',
        'City':'Dhaka',
        'name02':'Hossen',
        'department02':'English',
        'city02':'Narayangonj',
        
    }
    
    return render(request,'Third.html',myDict)







def no4(request):
    
    return render(request,'Fourth.html')

def no5(request):
    return render(request,'Fifth.html')