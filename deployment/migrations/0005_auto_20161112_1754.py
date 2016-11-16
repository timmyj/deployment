# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0004_machine_mac_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='machine_type',
            field=models.CharField(choices=[('Desktop', 'Desktop'), ('Laptop', 'Laptop')], default='Desktop', max_length=10, verbose_name='Machine Type'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='mac_address',
            field=models.CharField(blank=True, max_length=17, unique=True, verbose_name='MAC Address'),
        ),
    ]
