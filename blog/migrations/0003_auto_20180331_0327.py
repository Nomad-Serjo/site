# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-31 00:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180325_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 3, 31, 3, 27, 46, 174127), verbose_name='Опубликована'),
        ),
    ]
