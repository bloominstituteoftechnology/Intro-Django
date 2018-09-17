from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    # when added
    created_at = models.DateTimeField(auto_now_add=True)
    # when added or modified
    last_modified = models.DateTimeField(auto_now=True)


class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(
        'ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn" target="_blank">ISBN number</a>')
    first_edition = models.BooleanField()
    # year_published = models.DateField()
    summary = models.TextField(max_length=1000, blank=True)

    PAPERBACK = 'PB'
    HARDBACK = 'HB'
    TYPE_OF_BOOK_CHOICES = (
        (PAPERBACK, 'Paperback'),
        (HARDBACK, 'Hardback'),
    )
    type_of_book = models.CharField(
        max_length=2,
        choices=TYPE_OF_BOOK_CHOICES,
        default=PAPERBACK,
    )


class Illustrate(Book):
    illustrated = models.BooleanField()
