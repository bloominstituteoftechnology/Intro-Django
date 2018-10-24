from django.contrib import admin

from .models import Movies, Announcement, PersonalMovie


# Register your models here.

admin.site.register(Movies)
admin.site.register(PersonalMovie)
admin.site.register(Announcement)