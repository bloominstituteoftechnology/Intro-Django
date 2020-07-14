from django.contrib import admin

from .models import Player, PersonalPlayer

class PlayerAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(PersonalPlayer)