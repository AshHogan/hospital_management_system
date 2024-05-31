# core/admin.py
from django.contrib import admin
from .models import MedicalSupply

@admin.register(MedicalSupply)
class MedicalSupplyAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price']
