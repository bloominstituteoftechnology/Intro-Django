from django.db import models
from uuid import uuid4

class Entry(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid4, editable = False)
	item = models.CharField(max_length=200)
	servings = models.DecimalField(max_digits = 5, decimal_places=2)
	was_enjoyed = models.BooleanField()
	date_added = models.DateTimeField(auto_now_add=True)




