# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-27 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0003_auto_20180327_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=100, verbose_name=b"person's first name"),
        ),
    ]