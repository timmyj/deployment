# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0003_auto_20161112_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='mac_address',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='MAC Address'),
        ),
    ]
