from django.contrib import admin
from .models import *
# Register your models here.
@admin.register( Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','class_name','date_of_birth']