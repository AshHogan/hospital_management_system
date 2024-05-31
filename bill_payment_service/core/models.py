# core/models.py
from django.db import models

class Bill(models.Model):
    patient_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    due_date = models.DateField()

    def __str__(self):
        return f"Bill {self.id} for Patient {self.patient_id}"
