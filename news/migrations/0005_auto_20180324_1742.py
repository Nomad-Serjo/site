# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-24 14:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20180310_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 3, 24, 17, 42, 2, 765441), verbose_name='Опубликована'),
        ),
    ]