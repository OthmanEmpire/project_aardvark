# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-05 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20160505_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='isHistory',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
