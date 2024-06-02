from django.contrib import admin

# Register your models here.
from myApp.models import *

admin.site.register(studentmodel)
admin.site.register(doctormodel)
admin.site.register(teachermodel)
admin.site.register(table4model)
admin.site.register(table5model)
