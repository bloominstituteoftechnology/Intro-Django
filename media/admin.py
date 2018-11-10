from django.contrib import admin
from .models import Media, Book, Music, Movie, Reviewer
# Register your models here.
class MediaAdmin(admin.ModelAdmin):
	list_display = ('title', 'artist', 'year_pub', 'rating', 'type')
	readonly_fields=('created_at', 'last_modified')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'artist', 'year_pub', 'rating')
	readonly_fields=('created_at', 'last_modified')	

class MusicAdmin(admin.ModelAdmin):
	list_display = ('title', 'artist', 'year_pub', 'rating')
	readonly_fields=('created_at', 'last_modified')	

class MovieAdmin(admin.ModelAdmin):
	list_display = ('title', 'artist', 'year_pub', 'rating')
	readonly_fields=('created_at', 'last_modified')	

class ReviewerAdmin(admin.ModelAdmin):
	list_display = ('user', 'dob')


admin.site.register(Media, MediaAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Reviewer, ReviewerAdmin)
