from django.contrib import admin

# Register your models here.
from .models import Note

admin.site.register(Note)

#can register more in here with the .register() method.
