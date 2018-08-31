from django.contrib import admin

from .models import Beans, Equitment, Brew


class BrewAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


admin.site.register((Beans, Equitment, Brew), BrewAdmin)
