from django.contrib import admin
from .models import Company,Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display=('company_name','location','type','added_date')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('employee_name','email','phone','position','company')
# Register your models here.
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)