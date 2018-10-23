from django.contrib import admin

from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

admin.site.register(Book, BookAdmin)


