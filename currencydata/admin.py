from django.contrib import admin
from .models import Currencydata
from .models import PersonalCurrencydata
# Register your models here.
admin.site.register(Currencydata)
admin.site.register(PersonalCurrencydata)
