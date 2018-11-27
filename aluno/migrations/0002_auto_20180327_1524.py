# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-27 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='idade',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='numero_matricula',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='status',
        ),
        migrations.AddField(
            model_name='aluno',
            name='nascimento',
            field=models.CharField(default=b'', max_length=8),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nivel_conhecimento',
            field=models.CharField(choices=[(b'Excelente', b'Excelente'), (b'Bom', b'Bom'), (b'Regular', b'Regular'), (b'Ruim', b'Ruim')], max_length=100),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=100, verbose_name=b'Teste'),
        ),
    ]
