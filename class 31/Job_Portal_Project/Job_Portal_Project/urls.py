
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Job_Portal_Project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('signout/',signout,name="signout"),
    path('addjobpage/',addjobpage,name="addjobpage"),
    path('editprofile/',editprofile,name="editprofile"),
    path('index/',index,name="index"),
    path('joblist/',joblist,name="joblist"),
    path('profile/',profile,name="profile"),
    path('dashboard/',dashboard,name="dashboard"),
    path('updatejob/',updatejob,name="updatejob"),
    path('viewjob/<int:id>',viewjob,name="viewjob"),
    path('editjob/<int:myid>',editjob,name="editjob"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

