# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0005_auto_20150330_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='reference1_email',
            field=models.EmailField(default=b'', max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='reference2_email',
            field=models.EmailField(default=b'', max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='start_date',
            field=models.DateField(default=datetime.date(2015, 3, 31), blank=True),
        ),
    ]
