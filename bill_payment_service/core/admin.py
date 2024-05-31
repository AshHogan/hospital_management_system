# core/admin.py
from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'amount', 'is_paid', 'due_date']
