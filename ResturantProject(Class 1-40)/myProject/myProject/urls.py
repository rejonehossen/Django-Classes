from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name="signup"),
    path('signin/',signin,name="signin"),
    path('signout/',signout,name="signout"),
    
    # Index
    path('index/',index,name="index"),
    path('main/',main,name="main"),
    path('',hero,name="hero"),
    
    # Profile
    path('profile/',profile,name="profile"),
    path('editprofile/',editprofile,name="editprofile"),
    path('changepassword/',changepassword,name="changepassword"),
    
    
    # Recipe Section
    path('addrecipepage/',addrecipepage,name="addrecipepage"),
    path('editrecipe/<str:myid>',editrecipe,name="editrecipe"),
    path('recipelist/',recipelist,name="recipelist"),
    path('detailsrecipe/<str:myid>',detailsrecipe,name="detailsrecipe"),
    path('deleterecipe/<str:myid>',deleterecipe,name="deleterecipe"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
