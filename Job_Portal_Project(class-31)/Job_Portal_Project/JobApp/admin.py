from django.contrib import admin
from JobApp.models import *


class display(admin.ModelAdmin):
    list_display=[
        'username'
    ]
    
    
admin.site.register(customuser,display)
admin.site.register(addjob)
admin.site.register(recruiterprofile)
admin.site.register(seekerprofile)