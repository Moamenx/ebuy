# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-14 09:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_packagephotos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PackagePhotos',
            new_name='PackagePhoto',
        ),
        migrations.RenameModel(
            old_name='PackageProducts',
            new_name='PackageProduct',
        ),
        migrations.RenameModel(
            old_name='ProductPhotos',
            new_name='ProductPhoto',
        ),
    ]
