from django.contrib import admin

from .models import Note, Articles, PersonalNote, PersonalArticle


class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

class ArticleAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')


# Register your models here.
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)
admin.site.register(PersonalArticle)

admin.site.register(Articles, ArticleAdmin)