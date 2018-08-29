from django.db import models
from django.contrib.auth.models import User
from enum import Enum
from uuid import uuid4

# Create your models here.

class ColorChoice(Enum):
    W = "white"
    B = "black"
    R = "red"
    G = "green"
    U = "blue"

class TypeChoice(Enum):
    sorcery = "sorcery"
    instant = "instant"
    land = "land"
    creature = "creature"

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=128)
    cost = models.CharField(max_length=16)
    cmc = models.IntegerField()
    color = models.CharField(
        max_length = 32,
        choices= [(color.name, color.value) for color in ColorChoice]
    )
    cardType = models.CharField(
        max_length = 128,
        choices= [(ctype.name, ctype.value) for ctype in TypeChoice]
    )
    subType = models.CharField(max_length=32)
    cardSet = models.CharField(max_length=128)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserCollection(Card):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
"""
c = Card(name="Beejeezee", cost="w", color=ColorChoice.W, cmc=1, cardType=TypeChoice.creature, subType="bird", cardSet="the best set", text="Split Second\nWin the game.")

c = Card(name="Beejeezee", cost="w", color="white", cmc=1, cardType="creature", subType="bird", cardSet="the best set", text="Split Second\nWin the game.")
"""