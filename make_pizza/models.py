from django.db import models


class Toppings(models.Model):
    toppping = models.CharField(max_length=30)
    veg_meat= models.CharField(max_length=30)

# Create your models here.
class Pizza(models.Model):
    size = models.CharField(max_length=30)
    price = models.FloatField()
    toppings = models.ManyToManyField(Toppings)
    properity = models.CharField(max_length=300)
    special = models.CharField(max_length=200)
