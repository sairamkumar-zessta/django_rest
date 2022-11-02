from django.contrib import admin
from .models import Details
# Register your models here.


@admin.register(Details) 
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','date_of_birth','age']