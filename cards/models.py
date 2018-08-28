from django.db import models
# from enum import Enum
from uuid import uuid4
# Create your models here.
# class ColorChoice(Enum):
#     W = "white"
#     B = "black"
#     R = "red"
#     G = "green"
#     U = "blue"
# class TypeChoice(Enum):
#     sorcery = "sorcery"
#     instant = "instant"
#     land = "land"
#     creature = "creature"
class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=128)
    cost = models.CharField(max_length=16)
    color = models.CharField(
        max_length = 32,
        # choices= [(color, color.value) for color in ColorChoice]
    )
    cmc = models.IntegerField()
    cardType = models.CharField(
        max_length = 128,
        # choices= [(ctype, ctype.value) for ctype in TypeChoice]
    )
    subType = models.CharField(max_length=32)
    cardSet = models.CharField(max_length=128)
    text = models.TextField()

    def __str__(self):
        return self.name
"""
c = Card(name="Beejeezee", cost="w", color=ColorChoice.W, cmc=1, cardType=TypeChoice.creature, subType="bird", cardSet="the best set", text="Split Second\nWin the game.")
"""