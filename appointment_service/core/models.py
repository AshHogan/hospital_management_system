# core/models.py
from django.db import models

class Appointment(models.Model):
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Appointment {self.id} for Patient {self.patient_id} with Doctor {self.doctor_id}"
