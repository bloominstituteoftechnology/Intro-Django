from django.contrib import admin

# Register your models here.

from .models import Companies, StockPrices

admin.site.register(Companies)
admin.site.register(StockPrices)