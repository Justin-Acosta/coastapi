from django.db import models
from .location import Location
from .fish import Fish

class Population(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    quantity = models.IntegerField()