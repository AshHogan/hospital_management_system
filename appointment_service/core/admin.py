# core/admin.py
from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'doctor_id', 'date', 'time', 'status']
