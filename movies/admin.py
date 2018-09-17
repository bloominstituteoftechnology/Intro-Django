from django.contrib import admin
from .models import Movie, UserMovie

class MovieAdmin(admin.ModelAdmin):
  readonly_fields=('created_at', 'last_modified')

# Register your models here.

admin.site.register(Movie, MovieAdmin)
admin.site.register(UserMovie, MovieAdmin)