# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20180604_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='sar_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='sar_price',
            field=models.FloatField(default=0),
        ),
    ]
