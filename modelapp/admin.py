from django.contrib import admin
from .models import studentinfo

class Student(admin.ModelAdmin):
    list_display = ["name","surname","email","std"]

# Register your models here.
admin.site.register(studentinfo,Student)