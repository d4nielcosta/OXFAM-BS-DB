# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0009_auto_20150331_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='health_and_safety',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='risk_assessment',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
