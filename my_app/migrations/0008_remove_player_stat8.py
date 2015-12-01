# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_player_stat8'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='stat8',
        ),
    ]
