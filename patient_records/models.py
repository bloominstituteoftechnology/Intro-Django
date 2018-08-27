from django.db import models
from uuid import uuid4

class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    patient_name = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    PCP = models.CharField(blank=True, max_length=100)
    insurance = models.CharField(blank=True, max_length=500)
    medical_history = models.TextField(blank=True)
    drug_allergies = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
