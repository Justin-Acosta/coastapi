from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    location_id = models.IntegerField(null = True)
    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    image = models.ImageField(upload_to='player/',width_field=None, max_length=None, default='player/default.jpg')