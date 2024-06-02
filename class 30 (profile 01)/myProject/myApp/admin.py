from django.contrib import admin
from myApp.models import *

class displaylist(admin.ModelAdmin):
    list_display=['username','display_name']
    

admin.site.register(customuser,displaylist)
admin.site.register(addjobmodel)
admin.site.register(recruiterprofile)
admin.site.register(seekerprofile)
