# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170319_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.TimeField(null=True),
        ),
    ]