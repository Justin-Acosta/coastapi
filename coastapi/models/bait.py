from django.db import models

class Bait(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slots = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='bait/', width_field=None, max_length=None, null=True)
    red_modifier = models.DecimalField(max_digits=4, decimal_places=2)
    blue_modifier = models.DecimalField(max_digits=4, decimal_places=2)
    green_modifier = models.DecimalField(max_digits=4, decimal_places=2)
    yellow_modifier = models.DecimalField(max_digits=4, decimal_places=2)