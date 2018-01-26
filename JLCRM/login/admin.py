from django.contrib import admin
from login.models import Staff,Authority


# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ['username','password','name','gendar','age','education','qualification']

class AuthorityAdmin(admin.ModelAdmin):
    list_display = ['level','description']


admin.site.register(Staff, StaffAdmin)
admin.site.register(Authority, AuthorityAdmin)
