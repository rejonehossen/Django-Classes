
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home"),
    path('index/',index,name="index"),
    path('about/',about,name="about"),
    path('news/',news,name="news"),
    path('addstudentpage/',addstudentpage,name="addstudentpage"),
    path('doctortable/',doctortable,name="doctortable"),
    path('teachertable/',teachertable,name="teachertable"),
    path('doctorform/',doctorform,name="doctorform"),
    path('table5/',table5,name="table5"),
    path('table4/',table4,name="table4"),
    path('teacherform/',teacherform,name="teacherform"),
    path('table4form/',table4form,name="table4form"),
    path('table5form/',table5form,name="table5form"),
    
]
