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
admin.site.register(applyjobmodel)



admin.site.register(basicinformation)
admin.site.register(contact)
admin.site.register(educational_qualification)
admin.site.register(work_experience)