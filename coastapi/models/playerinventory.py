from django.db import models

class PlayerInventory(models.Model):
    id = models.AutoField(primary_key=True)
    slots = models.IntegerField()
    player_id = models.IntegerField()
    fish_id = models.IntegerField()