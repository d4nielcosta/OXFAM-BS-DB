# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0002_auto_20150330_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='reference1_forename',
            field=models.CharField(default=b'', max_length=128, blank=True),
        ),
    ]
