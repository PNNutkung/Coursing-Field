# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 05:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainmodels', '0006_auto_20161026_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
