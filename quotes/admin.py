from django.contrib import admin
from .models import Quote, PersonalQuote





# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

admin.site.register(Quote, QuoteAdmin)
admin.site.register(PersonalQuote)