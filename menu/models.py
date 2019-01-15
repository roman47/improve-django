from django.db import models
from django.utils import timezone
from datetime import timedelta, datetime


class Menu(models.Model):
    season = models.CharField(max_length=20)
    created_date = models.DateField(default=timezone.now)
    expiration_date = models.DateField(default=
                                       (datetime.now()+timedelta(days=365)))
    items = models.ManyToManyField('Item', related_name='items')

    def __str__(self):
        return self.season


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    chef = models.ForeignKey('auth.User')
    created_date = models.DateField(default=timezone.now)
    standard = models.BooleanField(default=False)
    ingredients = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name





