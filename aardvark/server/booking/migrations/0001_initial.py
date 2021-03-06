# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-03 03:01
from __future__ import unicode_literals

import booking.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('table', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=13)),
                ('date', models.DateField()),
                ('time', models.TimeField(choices=[(datetime.time(9, 0), datetime.time(9, 0)), (datetime.time(11, 0), datetime.time(11, 0)), (datetime.time(13, 0), datetime.time(13, 0)), (datetime.time(15, 0), datetime.time(15, 0))])),
                ('reference', models.CharField(default=booking.models._generateUniqueReferenceNumber, max_length=10)),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.Table')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
