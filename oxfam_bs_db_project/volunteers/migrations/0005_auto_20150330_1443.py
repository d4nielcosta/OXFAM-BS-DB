# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0004_auto_20150330_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='forename',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='surname',
            field=models.CharField(max_length=128),
        ),
    ]
