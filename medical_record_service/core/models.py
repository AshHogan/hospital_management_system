# core/models.py
from django.db import models

class MedicalRecord(models.Model):
    patient_id = models.IntegerField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    doctor_id = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Medical Record {self.id} for Patient {self.patient_id}"
