# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0007_volunteer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='address',
            field=models.TextField(default=b'', max_length=300, blank=True),
        ),
    ]
