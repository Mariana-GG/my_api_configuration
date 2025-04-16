from django.db import models

# Create your models here.


class Country(models.Model):
    short_name = models.CharField(max_length=10)
    full_name = models.CharField(max_length=100)
    capital = models.CharField(max_length=10)
    president = models.CharField(max_length=10, blank=True, null=True)
    population = models.IntegerField(default=0)
    currency = models.CharField(max_length=5)
    no_of_states = models.IntegerField(default=0)
