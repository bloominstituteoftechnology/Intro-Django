from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return (f"Title: {self.title} Content: {self.content}")
 
 # Inherits from Note!
class PersonalNote(Note):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# #What this is doing is importing Django’s built in user class model with
# something called a _foreign key_ to create a reference to data on another table.
# It works sort of like a pointer in C.
# `on_delete=models.CASCADE` helps with the integrity of the data.  In relational
# databases, one of the principles is to protect consistency.  There shouldn’t be
# an item in one table that references the foreign key of something that has been
# removed from another.  Check the readme in the repo for more info.