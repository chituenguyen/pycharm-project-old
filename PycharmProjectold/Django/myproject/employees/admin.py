from django.contrib import admin
from .models import Employee,Available_Jobs
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone_number','email_id']


@admin.register(Available_Jobs)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name']