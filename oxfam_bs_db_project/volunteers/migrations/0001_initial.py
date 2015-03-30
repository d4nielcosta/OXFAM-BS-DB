# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('forename', models.CharField(default=b'NO FORENAME ENTERED', max_length=128)),
                ('surname', models.CharField(default=b'NO SURNAME ENTERED', max_length=128)),
                ('primary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999'. Up to 15 digits allowed.")])),
                ('secondary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999'. Up to 15 digits allowed.")])),
                ('emergency_contact_forename', models.CharField(default=b'NO FORENAME ENTERED', max_length=128)),
                ('emergency_contact_surname', models.CharField(default=b'NO SURNAME ENTERED', max_length=128)),
                ('emergency_contact_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999'. Up to 15 digits allowed.")])),
                ('reference1_forename', models.CharField(default=b'', max_length=128, blank=True)),
                ('reference1_surname', models.CharField(default=b'', max_length=128, blank=True)),
                ('reference1_primary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999'. Up to 15 digits allowed.")])),
                ('reference1_secondary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999'. Up to 15 digits allowed.")])),
                ('reference2_forename', models.CharField(default=b'', max_length=128, blank=True)),
                ('reference2_surname', models.CharField(default=b'', max_length=128, blank=True)),
                ('reference2_primary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999'. Up to 15 digits allowed.")])),
                ('reference2_secondary_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format:'+999999999'. Up to 15 digits allowed.")])),
                ('start_date', models.DateField(blank=True)),
                ('birthday', models.DateField(blank=True)),
                ('parental_permission', models.BooleanField(default=False)),
                ('permission_to_work', models.BooleanField(default=False)),
                ('till', models.BooleanField(default=False)),
                ('open_shop', models.BooleanField(default=False)),
                ('close_shop', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
