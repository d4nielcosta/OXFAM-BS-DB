# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0002_volunteer_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='slug',
            field=models.SlugField(default=b'NO SLUG FIELD'),
            preserve_default=True,
        ),
    ]
