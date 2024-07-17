from django.db import models

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    nickname = models.CharField(max_length=255)
    location_id = models.IntegerField()
    wallet = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255)