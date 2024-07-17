from django.db import models

class Bait(models.Model):
    id = models.AutoField(primary_key=True)
    slots = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255)
    red_modifier = models.DecimalField(max_digits=10, decimal_places=2)
    blue_modifier = models.DecimalField(max_digits=10, decimal_places=2)
    green_modifier = models.DecimalField(max_digits=10, decimal_places=2)
    yellow_modifier = models.DecimalField(max_digits=10, decimal_places=2)