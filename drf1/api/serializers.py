from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length = 100)
    fathername = serializers.CharField(max_length = 100)
    classname = serializers.IntegerField()
    dateofbirth = serializers.DateField()