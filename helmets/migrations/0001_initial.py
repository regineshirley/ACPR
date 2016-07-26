# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-22 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Helmets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=1000)),
                ('item_number', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
