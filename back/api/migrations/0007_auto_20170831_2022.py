# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_merge_20170831_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dream',
            name='hospital_address',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Endereço (onde paciente está)'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='hospital_contact',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Contato do Hospital'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='hospital_name',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Nome do Hospital'),
        ),
    ]