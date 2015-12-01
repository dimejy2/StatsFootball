# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0013_auto_20151130_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='pos',
            field=models.CharField(default=datetime.datetime(2015, 12, 1, 2, 53, 35, 708014, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
