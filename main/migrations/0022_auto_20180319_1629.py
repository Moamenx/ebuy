# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-19 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_cart_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=17),
        ),
    ]
