# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-10 17:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0016_auto_20180510_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dia',
            old_name='day',
            new_name='dia',
        ),
    ]
