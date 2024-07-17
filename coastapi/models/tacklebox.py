from django.db import models

class TackleBox(models.Model):
    id = models.AutoField(primary_key=True)
    slots = models.IntegerField()
    player_id = models.IntegerField()
    bait_id = models.IntegerField()