# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-07 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_auto_20171227_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='versionedfile',
            name='metadata',
            field=models.TextField(blank=True, default=''),
        ),
    ]
