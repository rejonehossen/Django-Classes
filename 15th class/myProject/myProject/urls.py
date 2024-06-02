
from django.contrib import admin
from django.urls import path
from myProject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name="index"),
    path('teacherdata/',teacherdata,name="teacherdata"),
    path('addteacher/',addteacher,name="addteacher"),
    path('deleteteacher/<str:myid>',deleteteacher,name="deleteteacher"),
    path('editteacher/<str:myid>',editteacher,name="editteacher"),
    path('updateteacher/',updateteacher,name="updateteacher"),
    path('viewteacher/<str:myid>',viewteacher,name="viewteacher"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)