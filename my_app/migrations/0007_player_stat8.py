# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20151129_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='stat8',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
