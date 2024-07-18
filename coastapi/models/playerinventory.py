from django.db import models
from coastapi.models import Player,Fish

class PlayerInventory(models.Model):
    id = models.AutoField(primary_key=True)
    slots = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)