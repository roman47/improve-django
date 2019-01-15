# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-15 21:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20190115_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='menus',
        ),
        migrations.AddField(
            model_name='menu',
            name='items',
            field=models.ManyToManyField(to='menu.Item'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 15, 13, 37, 25, 407980)),
        ),
    ]
