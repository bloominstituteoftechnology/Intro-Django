from django.contrib import admin

from .models import ColorChoice
from .models import TypeChoice
from .models import Card
from .models import UserCollection

class CardAdmin(admin.ModelAdmin):
    exclude = ('cmc',)
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
# admin.site.register(ColorChoice, CardAdmin)
# admin.site.register(TypeChoice, CardAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(UserCollection, CardAdmin)