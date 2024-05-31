# core/views.py
from rest_framework import viewsets
from .models import MedicalSupply
from .serializers import MedicalSupplySerializer

class MedicalSupplyViewSet(viewsets.ModelViewSet):
    queryset = MedicalSupply.objects.all()
    serializer_class = MedicalSupplySerializer
