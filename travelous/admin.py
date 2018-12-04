from django.contrib import admin
from .models import Country, City


class CountryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "last_modified")


# Register your models here.
admin.site.register(Country, CountryAdmin)
admin.site.register(City)
