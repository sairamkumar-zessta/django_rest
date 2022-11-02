from .models import Details
from .serializers import StudentSerializer
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = StudentSerializer 