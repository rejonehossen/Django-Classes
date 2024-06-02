from django.contrib import admin
from myApp.models import *

class displaylist(admin.ModelAdmin):
    listitem=[
        'username','usertype'
    ]

admin.site.register(customuser,displaylist)
admin.site.register(recipemodel)