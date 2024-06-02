from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name="index"),
    path('data/',data,name="data"),
    path('add/',add,name="add"),
    path('update/',update,name="update"),
    path('delete/<str:myid>',delete,name="delete"),
    path('edit/<str:myid>',edit,name="edit"),
    path('view/<str:myid>',view,name="view"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
