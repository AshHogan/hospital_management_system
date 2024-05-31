# core/admin.py

from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'dob', 'email', 'phone_number', 'address']

admin.site.register(Patient, PatientAdmin)
