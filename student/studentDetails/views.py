from tkinter import Y
from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import studentDetailsSerializers
from .models import StudentDet
# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    queryset = StudentDet.objects.raw('SELECT * FROM public."studentDetails_studentdet" WHERE cast(to_char(date_of_birth,\'YYYY\') as integer) between 1998 and 2000;')
    serializer_class = studentDetailsSerializers
