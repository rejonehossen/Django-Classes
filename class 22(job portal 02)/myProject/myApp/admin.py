from django.contrib import admin
from myApp.models import *

class displaylist(admin.ModelAdmin):
    list_display=['username','display_name']
    

admin.site.register(customuser,displaylist)
