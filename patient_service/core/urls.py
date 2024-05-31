from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet
from .views import SetAppointmentView

router = DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('set_appointment/', SetAppointmentView.as_view(), name='set_appointment'),
]
