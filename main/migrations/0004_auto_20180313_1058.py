# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-13 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180313_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphotos',
            name='photo',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='productphotos',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product'),
        ),
    ]
