# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from uuid import uuid4
from django.db import models

# Create your models here.

class Pokemon(models.Model):
    NORMAL = 'NOR'
    FIRE = 'FIR'
    WATER = 'WAT'
    ELECTRIC = 'ELE'
    GRASS = 'GRA'
    ICE = 'ICE'
    FIGHTING = 'FIG'
    POISON = 'POI'
    GROUND = 'GRO'
    FLYING = 'FLY'
    PSYCHIC = 'PSY'
    BUG = 'BUG'
    ROCK = 'ROC'
    GHOST = 'GHO'
    DRAGON = 'DRA'
    DARK = 'DAR'
    STEEL = 'STE'
    FAIRY = 'FAI'

    TYPING = (
        (NORMAL, "Normal"),
        (FIRE, "Fire"),
        (WATER, "Water"),
        (ELECTRIC, "Electric"),
        (GRASS, "Grass"),
        (ICE, "Ice"),
        (FIGHTING, "Fighting"),
        (POISON, "POISON"),
        (GROUND, "Ground"),
        (FLYING, "Flying"),
        (PSYCHIC, "Psychic"),
        (BUG, "Bug"),
        (ROCK, "Rock"),
        (GHOST, "Ghost"),
        (DRAGON,"Dragon"),
        (DARK, "Dark"),
        (STEEL, "Steel"),
        (FAIRY, "Fairy")
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    primary = models.CharField(choices=TYPING, max_length=20)
    secondary = models.CharField(choices=TYPING, max_length=20)
    about = models.TextField(blank=True)