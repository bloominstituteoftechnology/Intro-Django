from django.contrib import admin
from .models import Game

class GameAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Game, GameAdmin)