# Generated by Django 4.2.13 on 2024-08-01 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bait',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(null=True, upload_to='bait/')),
                ('aggressive_modifier', models.DecimalField(decimal_places=2, max_digits=4)),
                ('curious_modifier', models.DecimalField(decimal_places=2, max_digits=4)),
                ('passive_modifier', models.DecimalField(decimal_places=2, max_digits=4)),
                ('skittish_modifier', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slots', models.IntegerField()),
                ('size', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(null=True, upload_to='fish/')),
            ],
        ),
        migrations.CreateModel(
            name='FishType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='location/')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slots', models.IntegerField(default=20)),
                ('progression', models.IntegerField(default=1)),
                ('nickname', models.CharField(max_length=255)),
                ('wallet', models.DecimalField(decimal_places=2, default=40.0, max_digits=10)),
                ('image', models.ImageField(default='player/default.jpg', upload_to='player/')),
                ('bait', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='coastapi.bait')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TackleBox',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('bait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coastapi.bait')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coastapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='ShopInventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coastapi.bait')),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coastapi.fish')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coastapi.location')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerInventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coastapi.fish')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coastapi.player')),
            ],
        ),
        migrations.AddField(
            model_name='fish',
            name='fish_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='coastapi.fishtype'),
        ),
    ]
