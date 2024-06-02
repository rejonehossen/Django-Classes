from django.shortcuts import render, redirect, HttpResponse

def homi(request):
    return HttpResponse("How are you")

def table(request):
    myDict={
        'name':'John Wick',
        'contact':542452553,
        'country':'Newyork',
        
    }
    return render(request,'table.html',myDict)

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def news(request):
    return render(request,'news.html')
