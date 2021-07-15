from django.contrib import admin
from .models import Client


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'data_create')


admin.site.register(Client, CompanyAdmin)

