# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-02 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20180502_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='equipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Equipe'),
        ),
    ]
