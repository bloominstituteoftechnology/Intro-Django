from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Companies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    ticker = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    shares_outstanding = models.DecimalField(max_digits=100000000000, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class StockPrices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    comp_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    close_price = models.DecimalField(max_digits=1000, decimal_places=2)
    adj_close = models.DecimalField(max_digits=1000, decimal_places=2) 
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

