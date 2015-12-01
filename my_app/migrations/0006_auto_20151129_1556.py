# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_player_stat4'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='stat5',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='player',
            name='stat6',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='player',
            name='stat7',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
