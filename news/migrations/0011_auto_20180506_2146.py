# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-06 18:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20180331_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 5, 6, 21, 46, 20, 828548), verbose_name='Опубликована'),
        ),
    ]
