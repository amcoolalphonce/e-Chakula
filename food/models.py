from django.db import models

class pizza(models.Model):
        name = models.CharField(max_length = 120)
        priceM = models.DecimalField(max_digits = 4, decimal_places =2)
        priceL = models.DecimalField(max_digits = 4, decimal_places = 2)
        pImage = models.URLField()
