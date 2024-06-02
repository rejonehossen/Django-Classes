
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home,name="home"),
    path('about', about,name="about"),
    path('contact', contact,name="contact"),
    path('news', news,name="news"),
    path('index', index,name="index"),
]
