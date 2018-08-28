from django.contrib import admin
from .models import Music

class MusicAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'last_modified')

#Register your models here.

admin.site.register(Music, MusicAdmin)
