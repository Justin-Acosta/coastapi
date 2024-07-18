from django.db import models
from coastapi.models import Player,Bait

class TackleBox(models.Model):
    id = models.AutoField(primary_key=True)
    slots = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    bait = models.ForeignKey(Bait, on_delete=models.CASCADE)