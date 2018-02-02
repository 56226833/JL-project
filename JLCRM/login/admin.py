from django.contrib import admin
from login import models


# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ['username','password','name','gendar','age','education','qualification','authority']

class AuthorityAdmin(admin.ModelAdmin):
    list_display = ['level','description']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','description','beginTime','endTime', 'contactor','staff']

class ContactorAdmin(admin.ModelAdmin):
    list_display = ['name','gendar','dialNumber','email']


admin.site.register(models.Staff, StaffAdmin)
admin.site.register(models.Authority, AuthorityAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Contactor, ContactorAdmin)
