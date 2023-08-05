# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partdistributor',
            old_name='manufacturer',
            new_name='distributor',
        ),
        migrations.AddField(
            model_name='partdistributor',
            name='part',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Part'),
        ),
        migrations.AddField(
            model_name='partmanufacturer',
            name='part',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Part'),
        ),
    ]
