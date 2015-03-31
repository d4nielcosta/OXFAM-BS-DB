# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0006_auto_20150331_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='address',
            field=models.CharField(default=b'', max_length=300, blank=True),
            preserve_default=True,
        ),
    ]
