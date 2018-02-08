from django.contrib import admin
from login import models


# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ['username','password','staff_name','staff_gendar','age','education','qualification','authority','amount','bonus','reimburse']

class AuthorityAdmin(admin.ModelAdmin):
    list_display = ['authority_level','authority_description']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name','project_description','beginTime','endTime', 'contactor','staff']

class ContactorAdmin(admin.ModelAdmin):
    list_display = ['contactor_name','contactor_gendar','contactor_dialNumber','contactor_email']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name','visits','lastVisitTime','intention','score']


admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Staff, StaffAdmin)
admin.site.register(models.Authority, AuthorityAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Contactor, ContactorAdmin)
