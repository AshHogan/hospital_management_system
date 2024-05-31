# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Doctor(AbstractUser):
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username
