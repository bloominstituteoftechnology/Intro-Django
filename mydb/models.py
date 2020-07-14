from django.db import models
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Dog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    sheds = models.BooleanField(default=True)
    playfulness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)
    activity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)
    affection = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)
    size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)
    other_pets = models.BooleanField(default=True)
    maintenance = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)
    climate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)

class ShelterDog(Dog):
    city = models.ForeignKey(User, on_delete=models.CASCADE)
