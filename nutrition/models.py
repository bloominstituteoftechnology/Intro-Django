from django.db import models

from datetime import datetime
from uuid import uuid4

# Create your models here.

###
 # @summary Model for the Meal class
 #
 # @description The Meal class is reponsible for creating new fields in the
 # nutrition.meals table in the database. Meals will contain nutrition facts
 # for all meals
 #
 # @author Brandon Benefield
 # @access public
 # @class Meal
 # @exports Meal
 # @extends models.Model
 ##
class Meal(models.Model):
    id       = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name     = models.CharField(max_length=50)
    date     = models.DateTimeField(default=datetime.now())
    calories = models.IntegerField()
    carbs    = models.IntegerField()
    protein  = models.IntegerField()


###
 # @summary Model for the Drink class
 #
 # @description The Drink class is reponsible for creating new fields in the
 # nutrition.drinks table in the database. Drinks will contain nutrition facts
 # for all drinks
 #
 # @author Brandon Benefield
 # @access public
 # @class Drink
 # @exports Drink
 # @extends models.Model
 ##
class Drink(models.Model):
    id       = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name     = models.CharField(max_length=50)
    date     = models.DateTimeField(default=datetime.now())
    calories = models.IntegerField()
    carbs    = models.IntegerField()
    protein  = models.IntegerField()