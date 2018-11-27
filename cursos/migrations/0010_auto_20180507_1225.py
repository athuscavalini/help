# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-07 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0012_auto_20180412_1800'),
        ('cursos', '0009_auto_20180425_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ListaPresenca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.Aluno')),
                ('days', models.ManyToManyField(to='cursos.Dia')),
            ],
        ),
        migrations.AddField(
            model_name='listapresenca',
            name='matriculas',
            field=models.ManyToManyField(to='cursos.Matricula'),
        ),
    ]
