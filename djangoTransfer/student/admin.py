from django.contrib import admin
from .models import StudentDetails
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(StudentDetails)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ['name','age','class_name','date_of_birth'] 