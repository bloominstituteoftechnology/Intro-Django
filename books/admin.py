from django.contrib import admin
from .models import Book, PersonalBook

# Register your models here.
admin.site.register(Book)
admin.site.register(PersonalBook)