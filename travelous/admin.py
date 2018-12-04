from django.contrib import admin
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "last_modified")


# Register your models here.
admin.site.register(Country, CountryAdmin)
