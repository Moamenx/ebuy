# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20180604_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bhd_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='jod_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='kwd_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='lbp_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='omr_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='qar_price',
            field=models.FloatField(default=0),
        ),
    ]
