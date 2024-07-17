from django.db import models

class Fish(models.Model):
    id = models.AutoField(primary_key=True)
    type_id = models.IntegerField()
    slots = models.IntegerField()
    size = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255)