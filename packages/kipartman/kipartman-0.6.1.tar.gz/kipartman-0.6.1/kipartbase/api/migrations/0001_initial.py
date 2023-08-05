# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.TextField()),
                ('uuid', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Footprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FootprintCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.FootprintCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True, default='', null=True)),
                ('octopart', models.TextField(blank=True, default=None, null=True)),
                ('updated', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.PartCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartDistributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packaging_unit', models.IntegerField()),
                ('item_price', models.FloatField()),
                ('currency', models.TextField()),
                ('package_price', models.FloatField()),
                ('sku', models.TextField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Distributor')),
            ],
        ),
        migrations.CreateModel(
            name='PartManufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.TextField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='PartParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('numeric', models.BooleanField()),
                ('text_value', models.TextField(blank=True, null=True)),
                ('min_value', models.FloatField(null=True)),
                ('nom_value', models.FloatField(null=True)),
                ('max_value', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('symbol', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='UnitPrefix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('symbol', models.TextField()),
                ('power', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='partparameter',
            name='max_exponent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='max', to='api.UnitPrefix'),
        ),
        migrations.AddField(
            model_name='partparameter',
            name='min_exponent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='min', to='api.UnitPrefix'),
        ),
        migrations.AddField(
            model_name='partparameter',
            name='nom_exponent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='nom', to='api.UnitPrefix'),
        ),
        migrations.AddField(
            model_name='partparameter',
            name='part',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Part'),
        ),
        migrations.AddField(
            model_name='partparameter',
            name='unit',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Unit'),
        ),
        migrations.AddField(
            model_name='part',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.PartCategory'),
        ),
        migrations.AddField(
            model_name='part',
            name='footprint',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Footprint'),
        ),
        migrations.AddField(
            model_name='part',
            name='parts',
            field=models.ManyToManyField(blank=True, to='api.Part'),
        ),
        migrations.AddField(
            model_name='footprint',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.FootprintCategory'),
        ),
    ]
