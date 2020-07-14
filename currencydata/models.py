from django.db import models
from django.utils import timezone 
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.
class Currencydata (models.Model):
    id = models.UUIDField(primary_key =True, default=uuid4, editable=False)
    date = models.CharField(max_length = 200)
    the_open = models.FloatField()
    the_high = models.FloatField()
    the_low = models.FloatField()
    the_close = models.FloatField()
    bar_type = models.CharField(max_length = 7)#'bull'  'bear'  'neutral'
    # created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    #Adjustment made because of error message received. 
    #the options auto_now auto_now_add and default 
    # are mutally exclusive only one of these options may be present.
    last_modified = models.DateTimeField(auto_now=True)

# End of Currencydata Class

#Personal(per-user)
class PersonalCurrencydata(Currencydata):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #What this is doing is importing Django's built in user class model with 
    #something called a foreign key to create a reference to data on another table.
    #On_delete=models.CASCADE helps with integrity of the data.  protect consistency.
    #There shouldn't be an item in one table that references the foreign key of something
    #that has been removed from another. 
#end of Personal Class
# Currencydata(date = '2018.09.12', the_open = 1.6963, the_high = 1.69636, the_low = 1.69596, the_close = 1.69619, bar_type = 'bear')
