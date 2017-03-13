# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=256)),
                ('content', models.CharField(max_length=4000)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]