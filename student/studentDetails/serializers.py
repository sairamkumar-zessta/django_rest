from rest_framework import serializers 
from .models import StudentDet
class studentDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentDet 
        fields = '__all__'