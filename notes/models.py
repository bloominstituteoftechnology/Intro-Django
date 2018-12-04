from django.db import models
from uuid import uuid4

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    # Model update
    # Now must makemigrations, then migrate
    date_created = models.DateTimeField(auto_now_add=True)
    last_editted = models.DateTimeField(auto_now=True)

class URLS(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

# In instances where Models need to be updated,
#  you must ./manage.py makemigration, then ./manage.py migrate to update the model

# models.Model
#   gives Django functionality 
#   eg access to fields such as UUIDField,Charfield, TextField, URLField

# The difference between ./manage.py shell and pipenv shell
#   think of scope locality

# One advantage to using Django, you can create data quick and easily in the ./manage.py shell
# Normally users would delete records manually through the GUI, but we can do it faster by filtering certain ID's in the shell

"""
for i in range(0, 40):
    n = Note(title=f"Title{i}", content="Details")
    # save() is inherited from models.Model
    # save() is the save button on the GUI
    n.save()
"""