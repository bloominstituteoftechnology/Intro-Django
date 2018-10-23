from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    yearPublished = models.CharField(max_length=10)
    pages = models.IntegerField(default=0)
    image = models.ImageField(upload_to='book_images', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)



class PersonalBook(Book):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
