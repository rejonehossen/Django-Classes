from django.contrib import admin
from myApp.models import *

class display_custom(admin.ModelAdmin):
    list_display=['username','usertype']
    
class display_recipe(admin.ModelAdmin):
    list_display=['recipe_title','created_by']
    
admin.site.register(customuser,display_custom)
admin.site.register(addrecipe,display_recipe)
admin.site.register(basicinformation)
admin.site.register(chefprofile)
admin.site.register(viewerprofile)