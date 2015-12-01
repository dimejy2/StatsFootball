# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_player_stat3'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='stat4',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
