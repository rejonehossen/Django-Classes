from django.shortcuts import render, redirect, HttpResponse

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')
def news(request):
    return render(request,'news.html')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')