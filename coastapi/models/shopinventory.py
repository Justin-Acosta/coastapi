from django.db import models

class ShopInventory(models.Model):
    id = models.AutoField(primary_key=True)
    player_id = models.IntegerField()
    bait_id = models.IntegerField()