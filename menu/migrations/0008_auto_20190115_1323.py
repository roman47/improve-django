# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-15 21:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20190115_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_on_menu',
            field=models.ManyToManyField(through='menu.MenuItem', to='menu.Menu'),
        ),
        migrations.AddField(
            model_name='menu',
            name='has_items',
            field=models.ManyToManyField(through='menu.MenuItem', to='menu.Item'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 15, 13, 23, 15, 679240)),
        ),
    ]