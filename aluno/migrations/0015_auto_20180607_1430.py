# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-07 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0014_auto_20180604_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='complemento',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
    ]
