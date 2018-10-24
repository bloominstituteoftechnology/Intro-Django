from django.contrib import admin

from .models import Movies, Announcement


# Register your models here.

admin.site.register(Movies)
admin.site.register(Announcement)