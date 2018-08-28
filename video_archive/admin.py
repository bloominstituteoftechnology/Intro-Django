from django.contrib import admin
from .models import Video, PersonalVideo


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "last_updated")


# Register your models here.

admin.site.register(Video, VideoAdmin)
admin.site.register(PersonalVideo)
