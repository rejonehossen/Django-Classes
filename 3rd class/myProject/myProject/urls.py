
from django.contrib import admin
from django.urls import path
from myProject.views import homepage,no2,no3,no4,no5
urlpatterns = [
    path('admin/', admin.site.urls),
   path('homepage',homepage),
    path('no2',no2,name="no2"),
    path('no3',no3,name="no3"),
    path('no4',no4,name="no4"),
    path('no5',no5,name="no5"),
]
