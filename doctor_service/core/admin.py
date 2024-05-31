# core/admin.py
from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['username', 'specialty', 'phone_number', 'email']
