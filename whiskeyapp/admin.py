from django.contrib import admin
from .models import Whiskey, PersonalWhiskey

class WhiskeyAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Whiskey, WhiskeyAdmin)
admin.site.register(PersonalWhiskey, WhiskeyAdmin)