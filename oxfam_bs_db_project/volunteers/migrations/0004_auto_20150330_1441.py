# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0003_auto_20150330_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='start_date',
            field=models.DateField(default=datetime.date(2015, 3, 30), blank=True),
        ),
    ]
