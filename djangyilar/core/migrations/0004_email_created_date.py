# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170313_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
