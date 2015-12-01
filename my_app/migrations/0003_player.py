# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20151104_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('stat1', models.CharField(max_length=30, blank=True)),
                ('stat2', models.CharField(max_length=30, blank=True)),
            ],
        ),
    ]
