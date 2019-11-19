from django.contrib import admin
from .models import Note, PersonalNote

# Register Note Model
admin.site.register(Note)

# Register PersonalNote
admin.site.register(PersonalNote) 

# MVP day 2 complete