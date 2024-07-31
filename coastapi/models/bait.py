from django.db import models

class Bait(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='bait/', width_field=None, max_length=None, null=True)
    aggressive_modifier = models.DecimalField(max_digits=4, decimal_places=2)
    curious_modifier = models.DecimalField(max_digits=4, decimal_places=2)
    passive_modifier = models.DecimalField(max_digits=4, decimal_places=2)
    skittish_modifier = models.DecimalField(max_digits=4, decimal_places=2)