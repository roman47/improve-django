# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-15 21:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20190115_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 15, 13, 23, 24, 388462)),
        ),
    ]
