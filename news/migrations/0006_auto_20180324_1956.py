# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-24 16:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180324_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 3, 24, 19, 56, 18, 504243), verbose_name='Опубликована'),
        ),
    ]
