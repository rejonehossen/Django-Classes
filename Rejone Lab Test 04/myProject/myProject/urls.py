from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('signout/',signout,name="signout"),
    
    
    path('dashboard/',dashboard,name="dashboard"),
    path('profile/',profile,name="profile"),
    
    
    
    path('addrecipe/',addrecipe,name="addrecipe"),
    
    
    
    
    path('listrecipe/',listrecipe,name="listrecipe"),
    
    
    path('viewrecipe/<str:myid>',viewrecipe,name="viewrecipe"),
    path('deleterecipe/<str:myid>',deleterecipe,name="deleterecipe"),
    path('editrecipe/<str:myid>',editrecipe,name="editrecipe"),
    
    
    path('updaterecipe/',updaterecipe,name="updaterecipe"),
    path('listrecipeforviewer/',listrecipeforviewer,name="listrecipeforviewer"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
