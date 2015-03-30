# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='slug',
            field=models.SlugField(default=b'NO SLUG FIELD'),
            preserve_default=True,
        ),
    ]
