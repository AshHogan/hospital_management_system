# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicalSupplyViewSet

router = DefaultRouter()
router.register(r'medical_supplies', MedicalSupplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
