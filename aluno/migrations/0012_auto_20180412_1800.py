# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-12 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0011_auto_20180411_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='celular',
            field=models.CharField(blank=True, default=b'', max_length=12),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nascimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]