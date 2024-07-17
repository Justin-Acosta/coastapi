from django.db import models

class Population(models.Model):
    id = models.AutoField(primary_key=True)
    location_id = models.IntegerField()
    fish_id = models.IntegerField()
    quantity = models.IntegerField()