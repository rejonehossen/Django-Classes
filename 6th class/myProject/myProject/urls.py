
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',index,name="index"),
    path('home',home,name="home"),
    path('table',table,name="table"),
    path('student',student,name="student"),
    path('teacher',teacher,name="teacher"),
    path('third',third,name="third"),
]
