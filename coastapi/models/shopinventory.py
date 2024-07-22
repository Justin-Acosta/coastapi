from django.db import models
from .player import Player
from .bait import Bait

class ShopInventory(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    bait = models.ForeignKey(Bait, on_delete=models.CASCADE)