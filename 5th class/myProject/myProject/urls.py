
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homi',homi,name="homi"),
    path('table',table,name="table"),
    path('index',index,name="index"),
    path('home',home,name="home"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('news',news,name="news"),
]
