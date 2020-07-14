from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from uuid import uuid4

# Create your models here.

class Meal(models.Model):
    '''
    Model for the Meal class

    The Meal class is reponsible for creating new fields in the
    nutrition.meals table in the database. Meals will contain nutrition facts
    for all drinks

    Attributes
    ----------
    id : uuid.UUID
        ranomized identifier using `uuid4`

    type : str
        type of meal (Food, Drink, Alternative)

    name : str
        name of meal

    date : datetime.datetime
        time of meal

    calories : int
        calories per meal

    carbs : int
        carbs per meal

    protein : int
        protein per meal
    '''
    
    id       = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    type     = models.CharField(max_length=50)
    name     = models.CharField(max_length=50)
    date     = models.DateTimeField(auto_now_add=True)
    calories = models.IntegerField()
    carbs    = models.IntegerField()
    protein  = models.IntegerField()


class PersonalMeal(Meal):
    '''
    Model for the PersonalMeal class

    The PersonalMeal class is responsible for creating a new table and field
    that a single user can perform CRUD operations on to more closely keep
    track of their meals. The PersonalMeal class extends the Meal class
    and contains all properties/methods as the Meal class

    Attributes
    ----------
    user : user
        key that corresponds to a user in the User table
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# class Drink(Meal):
#     '''
#     Model for the Drink class

#     The Drink class is reponsible for creating new fields in the
#     nutrition.drinks table in the database. Drinks will contain nutrition facts
#     for all drinks

#     Attributes
#     ----------
#     id : uuid.UUID
#         randomized identifier using `uuid4` 

#     name : str
#         name of the drink

#     date : datetime.datetime
#         date and time of drink

#     calories : integer
#         number of calories from drink

#     carbs : integer
#         number of carbs from drink

#     protein : integer
#         amount of protein from drink
#     '''
    
#     id       = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     name     = models.CharField(max_length=50)
#     date     = models.DateTimeField(auto_now_add=True)
#     calories = models.IntegerField()
#     carbs    = models.IntegerField()
#     protein  = models.IntegerField()