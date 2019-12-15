# https://docs.djangoproject.com/en/2.1/topics/db/models/

# https://www.mercurytide.co.uk/media/resources/django-cheat-sheet.pdf

# add images to model
# https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield


from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    author = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 75)
#    image = ImageField(blank = True, null = True)


#make a subclass of posts
class UserPost(Post):  #inherit properties from Note
    # use foreign key to create a reference to another table
    # CASCADE allows data to be consistent so that when a record is removed, related data will also be removed
    user = models.ForeignKey(User, on_delete = models.CASCADE)


