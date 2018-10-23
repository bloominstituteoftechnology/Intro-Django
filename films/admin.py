from django.contrib import admin
from .models import Film, PersonalFilm


class FilmAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Film, FilmAdmin)
admin.site.register(PersonalFilm)