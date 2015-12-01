# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='stat3',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
