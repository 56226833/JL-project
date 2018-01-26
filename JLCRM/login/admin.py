from django.contrib import admin
from login.models import Contactor


# Register your models here.
class ContactorAdmin(admin.ModelAdmin):
    list_display = ['name','gendar','dialNumber','email']


admin.site.register(Contactor, ContactorAdmin)
