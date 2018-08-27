from django.contrib import admin
from .models import Note
from .models import PersonalNote

admin.site.register((Note, PersonalNote))
