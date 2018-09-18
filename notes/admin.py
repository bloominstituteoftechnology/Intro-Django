from django.contrib import admin
from .models import Note, Movie, PersonalNote, FavoriteMovies, Brewery, Beer

class NoteAdmin(admin.ModelAdmin):
    readonly_fields= ('created_at', 'last_modified')

class MovieAdmin(admin.ModelAdmin):
    readonly_fields= ['created_at']    

class BreweryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')

# Register your models here.
admin.site.register(Note, NoteAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Brewery, BreweryAdmin)
admin.site.register(PersonalNote)
admin.site.register(FavoriteMovies)
admin.site.register(Beer)