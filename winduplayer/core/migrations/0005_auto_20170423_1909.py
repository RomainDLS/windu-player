# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170417_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(default=' - ', max_length=9, null=True),
        ),
    ]
