from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
import requests
from rest_framework.response import Response
from rest_framework.views import APIView

class SetAppointmentView(APIView):
    def post(self, request):
        patient_id = request.data.get('patient_id')
        appointment_data = {
            'date': request.data.get('date'),
            'time': request.data.get('time'),
            'doctor_id': request.data.get('doctor_id'),
        }
        response = requests.post('http://appointment_service/api/appointments/', data=appointment_data)
        return Response(response.json(), status=response.status_code)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
