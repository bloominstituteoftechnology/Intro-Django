from django.db import models
from uuid import uuid4
# Create your models here.
class Currencydata (models.Model):
    id = models.UUIDField(primary_key =True, default=uuid4, editable=False)
    date = models.CharField(max_length = 200)
    the_open = models.FloatField()
    the_high = models.FloatField()
    the_low = models.FloatField()
    the_close = models.FloatField()
    bar_type = models.CharField(max_length = 7)#'bull'  'bear'  'neutral'

# Currencydata(date = '2018.09.12', the_open = 1.6963, the_high = 1.69636, the_low = 1.69596, the_close = 1.69619, bar_type = 'bear')
