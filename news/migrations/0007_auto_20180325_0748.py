# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-25 04:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20180324_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 3, 25, 7, 48, 44, 453228), verbose_name='Опубликована'),
        ),
    ]
