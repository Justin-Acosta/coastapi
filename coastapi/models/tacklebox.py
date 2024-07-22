from django.db import models
from .bait import Bait

class TackleBox(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    bait = models.ForeignKey(Bait, on_delete=models.CASCADE)
    quantity = models.IntegerField()