# core/admin.py
from django.contrib import admin
from .models import MedicalRecord

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'diagnosis', 'treatment', 'doctor_id', 'date']
