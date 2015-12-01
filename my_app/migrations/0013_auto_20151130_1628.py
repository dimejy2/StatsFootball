# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0012_auto_20151130_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='stat1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='stat2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='stat3',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='stat4',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='stat5',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='stat6',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='stat7',
            field=models.FloatField(null=True),
        ),
    ]
