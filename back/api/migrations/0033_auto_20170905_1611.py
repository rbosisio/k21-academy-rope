# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20170905_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dream',
            name='impediment_days',
        ),
        migrations.RemoveField(
            model_name='dream',
            name='significative_days',
        ),
        migrations.AddField(
            model_name='dream',
            name='provisional_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Data prevista para realização'),
        ),
        migrations.AddField(
            model_name='dream',
            name='significative_and_impediment_days',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Data importante para o sonho ou dias no qual o sonho não pode ser realizado (Dias de tratamento, etc)'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='has_specific_dream',
            field=models.BooleanField(default=False, verbose_name='Ajuda com um sonho específico?'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='money_help',
            field=models.BooleanField(default=False, verbose_name='Ajuda com recusos financeiros?'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='observation',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Observações extras'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='status',
            field=models.CharField(blank=True, choices=[('novo', 'Novo'), ('aprovado', 'Aprovado'), ('reprovado', 'Reprovado')], default='novo', max_length=20, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='personal_characteristics',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Características pessoais (tímido, engraçado, paciente, etc)'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='status',
            field=models.CharField(blank=True, choices=[('novo', 'Novo'), ('aprovado', 'Aprovado'), ('reprovado', 'Reprovado')], default='novo', max_length=20, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='talents',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Talentos (Profissão, o que faz bem, o que gosta de fazer, etc)'),
        ),
    ]
