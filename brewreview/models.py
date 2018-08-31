from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class Beans(models.Model):
    beans_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    roaster = models.CharField(max_length=30)
    date_purchased = models.DateField()
    date_roasted = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.name}>'


class Equitment(models.Model):
    equitment_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    e_type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.make} {self.model}>'


class Brew(models.Model):
    brew_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beans_used = models.ForeignKey(Beans, on_delete=models.CASCADE)
    equitment_used = models.ForeignKey(Equitment, on_delete=models.CASCADE)
    mass_beans = models.PositiveSmallIntegerField()
    mass_water = models.PositiveSmallIntegerField()
    brew_time = models.DurationField()
    comments = models.CharField(max_length=200)

    # review choices taken directly from the docs
    # https://docs.djangoproject.com/en/2.1/ref/models/fields/
    AWFUL = 'AW'
    BAD = 'BD'
    OK = 'OK'
    GOOD = 'GD'
    AMAZING = 'AG'
    REVIEW_CHOICES = (
        (AWFUL, 'Awful'),
        (BAD, 'Bad'),
        (OK, 'Ok'),
        (GOOD, 'Good'),
        (AMAZING, 'Amazing'),
    )
    review = models.CharField(
        max_length=2,
        choices=REVIEW_CHOICES,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.brew_id}'
