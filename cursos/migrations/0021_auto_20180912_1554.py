# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-12 18:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0020_auto_20180912_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matricula',
            old_name='situcao',
            new_name='situacao',
        ),
    ]
