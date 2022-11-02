from functools import partial
from msilib.schema import ServiceInstall
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from api import serializers
from rest_framework import status
from rest_framework.views import APIView
# Function Based api_view
@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'POST':
        print(request.data)
        return Response({'msg' :'Post Request', 'data' : request.data})
    elif request.method == 'GET':
        return Response({'msg' : 'Hello world'})

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_details_func(request,pk=None):
    if request.method == 'GET' :
        req = pk
        if req is not None:
            stu = Student.objects.get(id = req)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many =True)
        return Response(serializer.data)


    if request.method == 'POST' :
        serializer = StudentSerializer( data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT' :
        req = pk
        stu = Student.objects.get(id = req)
        serializer = StudentSerializer( stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'},status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors)


    if request.method == 'DELETE' :
        req = pk
        stu = Student.objects.get(id = req)
        stu.delete()
        return Response({ 'msg' : 'Data Deleted'})

    if request.method == 'PATCH' :
        req = pk
        stu = Student.objects.get(id = req)
        serializer = StudentSerializer( stu, data = request.data ,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
# Class Based api_view
class StudentAPI(APIView):
    def get(self, request, format=None,pk=None):
        req = pk
        if req is not None:
            stu = Student.objects.get(id = req)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many =True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = StudentSerializer( data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put (self,request,format=None,pk=None):
        req = pk
        stu = Student.objects.get(id = req)
        serializer = StudentSerializer( stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors)

    def delete(self,request,format=None,pk=None):
        req = pk
        stu = Student.objects.get(id = req)
        stu.delete()
        return Response({ 'msg' : 'Data Deleted'})

    def patch(self,request,format=None,pk=None):
        req = pk
        stu = Student.objects.get(id = req)
        serializer = StudentSerializer( stu, data = request.data ,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
