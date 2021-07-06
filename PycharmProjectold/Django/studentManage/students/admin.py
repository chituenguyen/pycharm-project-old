from django.contrib import admin
from .models import student
# Register your models here.
# @admin.register(student)
# class studentAdmin(admin.ModelAdmin):
#     list_display = ['first_name','last_name','email_id','phone_number']
admin.site.register(student)
