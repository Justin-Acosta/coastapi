from django.db import models
from coastapi.models import Location,Fish

class Population(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    quantity = models.IntegerField()