# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-22 22:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helmets', '0003_helmetsmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HelmetsModel',
        ),
    ]
