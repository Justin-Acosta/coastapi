from django.db import models
from .player import Player
from .fish import Fish

class PlayerInventory(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)