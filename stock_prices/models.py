from django.db import models
from uuid import uuid4

# Create your models here.
class Companies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable-False)
    name = models.CharField(max_length=200)
    



# class StockPrices(models.Model):
#     comp_id = models.
#     date = models.
#     close_price = 
#     adj_close = 

