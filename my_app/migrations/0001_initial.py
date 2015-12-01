# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('identifier', models.CharField(max_length=3)),
                ('long_name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('id_2', models.CharField(max_length=3)),
                ('rate', models.FloatField(default=1.0)),
                ('last_update_time', models.DateTimeField()),
                ('id_1', models.ForeignKey(to='my_app.Currency')),
            ],
        ),
    ]
