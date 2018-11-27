# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-03 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0008_auto_20180403_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(help_text=b'Apenas os 11 numeros do CPF', max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nascimento',
            field=models.DateField(help_text=b'Digitar no modelo Dia/Mes/Ano'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(max_length=12),
        ),
    ]