# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_products_is_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
