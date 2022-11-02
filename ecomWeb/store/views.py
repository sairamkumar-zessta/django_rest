from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


# class CustomerModelViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all() 
#     serializer_class = CustomerSerializer 

class CartModelViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all() 
    serializer_class = CartSerializer

@api_view(['GET','POST'])
def customer_details_func(request,pk=None):
    if request.method == 'GET' :
        stu = Customer.objects.all()
        serializer = CustomerSerializer(stu , many =True)
        return Response(serializer.data)

    if request.method == 'POST' :
        serializer = CustomerSerializer( data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

