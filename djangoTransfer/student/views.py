from django.shortcuts import render
from .models import StudentDetails 
from rest_framework import viewsets 
from .serializers import StudentSerializer
# Create your views here.

class StudentView(viewsets.ModelViewSet):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentSerializer 