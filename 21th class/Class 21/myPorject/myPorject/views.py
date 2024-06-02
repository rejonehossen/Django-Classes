from django.shortcuts import render, redirect, HttpResponse

def signup(request):
    
    return render(request,'signup.html')



def signin(request):
    
    return render(request,'signin.html')