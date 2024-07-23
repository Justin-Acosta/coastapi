from django.db import models
from django.contrib.auth.models import User
from .location import Location
from .bait import Bait
from .tacklebox import TackleBox


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slots = models.IntegerField(default=20)
    progression = models.IntegerField(default=1)
    nickname = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, default=1)
    bait = models.ForeignKey(Bait,on_delete=models.DO_NOTHING, null=True)
    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    image = models.ImageField(upload_to='player/',width_field=None, max_length=None, default='player/default.jpg')

    @property
    def player_tacklebox(self):
        tacklebox = TackleBox.objects.filter(player=self)
        return tacklebox
