from rest_framework import serializers 
from .models import StudentDetails
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'