# Load our models related tables with admin site
from django.contrib import admin
from OneToOne_App.models import Student,Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'sname','marks','address']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','cname','cfee']

admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
