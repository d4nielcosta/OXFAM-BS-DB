# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0008_auto_20150331_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='reference1_received',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='reference1_sent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='reference2_received',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='reference2_sent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
