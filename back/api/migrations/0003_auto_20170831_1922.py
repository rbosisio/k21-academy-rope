# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170831_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='dream',
            name='contact_name',
            field=models.CharField(default=None, max_length=255, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='dream',
            name='dream_report',
            field=models.TextField(default=None, verbose_name='Relato do Sonho'),
        ),
        migrations.AddField(
            model_name='dream',
            name='health_conditions',
            field=models.TextField(default=None, verbose_name='Condições Médicas e Expectativa'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='description',
            field=models.TextField(default=None, verbose_name='Descrição do Sonho'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='hospital_address',
            field=models.CharField(default=None, max_length=255, verbose_name='Endereço (onde paciente está)'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='Nome do Paciente'),
        ),
    ]
