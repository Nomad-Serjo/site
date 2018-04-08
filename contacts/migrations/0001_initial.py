# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-31 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'посетитель',
                'verbose_name_plural': 'список рассылки',
            },
        ),
    ]
