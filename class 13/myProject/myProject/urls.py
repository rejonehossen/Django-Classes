from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name="index"),
    path('studentss/',studentss,name="studentss"),
    path('teacher/',teacher,name="teacher"),
    path('addstudent/',addstudent,name="addstudent"),
    path('addteacher/',addteacher,name="addteacher"),
    
    path('deletestudent/<str:myid>',deletestudent,name="deletestudent"),
    path('deleteteacher/<str:myid>',deleteteacher,name="deleteteacher"),
    path('editstudent/<str:myid>',editstudent,name="editstudent"),
    path('edittreacher/<str:myid>',edittreacher,name="edittreacher"),
    path('updatestudent',updatestudent,name="updatestudent"),
    path('updateteacher/',updateteacher,name="updateteacher"),
    
    path('viewteacher/<str:myid>',viewteacher,name="viewteacher"),
    path('viewstudent/<str:myid>',viewstudent,name="viewstudent"),
    
]
