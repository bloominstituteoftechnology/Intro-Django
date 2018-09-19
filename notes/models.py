from django.db import models
from uuid import uuid4
# Create your models here.

from django.contrib.auth.models import User

class Note(models.Model):
    NOTE_TYPE = (
        ('TD', 'To-Do'),
        ('WS', 'Words of Wisdom'),
        ('NS', 'Nonsense')
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    note_tag = models.CharField(
        max_length=2,
        choices=NOTE_TYPE,
        default='NS'
    )

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Band(models.Model):
    # For CharField type_of_music
    ROCK = 'RO'
    JAZZ = 'JA'
    FUNK = 'FU'
    COUNTRY = 'CO'
    MUSIC_TYPE = (
        (ROCK, 'Rock'),
        (JAZZ, 'Jazz'),
        (FUNK, 'Funk'),
        (COUNTRY, 'Country'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    members = models.TextField(blank=True)
    still_touring = models.BooleanField(default=False)
    type_of_music = models.CharField(
        max_length=2,
        choices=MUSIC_TYPE,
        default=ROCK,
    )
    pertinent_website = models.URLField(default="https://www.rockarchive.com/artists")
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

class FunkBand(Band):
    lead_singer = models.TextField(blank=True)