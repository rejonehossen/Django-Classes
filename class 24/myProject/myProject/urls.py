from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin,name="signin"),
    path('logout/',logout,name="logout"),
    path('signup/',signup,name="signup"),
    path('dashboard/',dashboard,name="dashboard"),
    path('index/',index,name="index"),
    path('viewjob/',viewjob,name="viewjob"),
    path('addjob/',addjob,name="addjob"),
    path('recentjob/',recentjob,name="recentjob"),
    path('appliedjob/',appliedjob,name="appliedjob"),
    # path('profile/',profile,name="profile"),
    path('profile/',profile,name="profile"),
    
    path('deletejob/<str:myid>',deletejob,name="deletejob"),
    path('detailsjob/<str:myid>',detailsjob,name="detailsjob"),
    path('editjob/<str:myid>',editjob,name="editjob"),

    path('updatejob/',updatejob,name="updatejob"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
