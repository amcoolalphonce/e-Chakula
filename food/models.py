from django.db import models

class Pizza(models.Model):# should begin with a capital yawa
        name = models.CharField(max_length = 120)
        priceM = models.DecimalField(max_digits = 4, decimal_places =2)
        priceL = models.DecimalField(max_digits = 4, decimal_places = 2)
        pImage = models.URLField()


class Beverages(models.Model):# should begin with a capital yawa
        name = models.CharField(max_length = 120)
        price = models.DecimalField(max_digits = 4, decimal_places =2)
        bImage = models.URLField()

class Dishes(models.Model):
        name = models.CharField(max_length = 120)
        price= models.DecimalField(max_digits = 4, decimal_places =2)
        dImage = models.URLField()

