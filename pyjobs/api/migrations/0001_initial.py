# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-07 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=250)),
            ],
        ),
    ]
