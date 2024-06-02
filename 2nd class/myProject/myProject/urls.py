
from django.contrib import admin
from django.urls import path
from myProject.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage', homePage,name="homePage"),
    path('contactpage', contactpage,name="contactpage"),
    path('thirdpage', thirdpage,name="thirdpage"),
    path('fourthpage', fourthpage,name="fourthpage"),
    path('fifthpage', fifthpage,name="fifthpage"),
    path('sixthpage', sixthpage,name="sixthpage"),
    path('seventhpage', seventhpage,name="seventhpage"),
    path('eighthpage', eighthpage,name="eighthpage"),
    path('ninthpage', ninthpage,name="ninthpage"),
]
