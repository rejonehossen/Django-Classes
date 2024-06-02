from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin,name="signin"),
    path('signup',signup,name="signup"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
