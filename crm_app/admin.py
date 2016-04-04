from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'sector', 'number_of_employees']

admin.site.register(Company, CompanyAdmin)
