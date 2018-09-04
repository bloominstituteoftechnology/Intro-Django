from django.contrib import admin
from .models import Deck, UserDeck

class DeckAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register((Deck, UserDeck), DeckAdmin)
