# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-14 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0023_auto_20180914_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turma',
            options={'ordering': ['-created_at'], 'verbose_name': 'Turma', 'verbose_name_plural': 'Turmas'},
        ),
    ]