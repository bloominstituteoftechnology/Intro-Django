from django.contrib import admin

# Register your models here.
from .models import Author, Note

admin.site.register(Author)
admin.site.register(Note)

