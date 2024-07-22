from django.db import models


class Fish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    fish_type = models.ForeignKey("FishType", on_delete=models.DO_NOTHING, null=True)
    slots = models.IntegerField()
    size = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='fish/',width_field=None, max_length=None, null=True)