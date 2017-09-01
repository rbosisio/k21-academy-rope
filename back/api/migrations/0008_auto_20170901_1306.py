# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170831_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dream',
            name='status',
            field=models.CharField(choices=[('novo', 'Novo'), ('inviavel', 'Inviavel'), ('pre_aprovado', 'Pré-Aprovado')], default='novo', max_length=20, verbose_name='Status'),
        ),
    ]