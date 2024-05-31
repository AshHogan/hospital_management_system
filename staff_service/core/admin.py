# core/admin.py
from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['username', 'role', 'phone_number', 'email']
