from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name_company', 'data_create')


admin.site.register(Company, CompanyAdmin)
