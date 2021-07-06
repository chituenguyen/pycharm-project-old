from django.contrib import admin
from .models import student,course,Destination
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','birthday','email','course_student']
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','type']
class destinationAdmin(admin.ModelAdmin):
    list_display = ['name','img','desc','price','offer']
admin.site.register(student,StudentAdmin)
admin.site.register(course,CourseAdmin)
admin.site.register(Destination,destinationAdmin)