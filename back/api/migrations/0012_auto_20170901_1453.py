# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20170901_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='dream',
            name='dream_needs',
            field=models.TextField(default=None, verbose_name='Necessidades do Sonho'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='category',
            field=models.CharField(choices=[('sonho_ir', 'Sonho Ir'), ('sonho_ir', 'Sonho Ir'), ('sonho_fazer', 'Sonho Fazer'), ('sonho_conhecer_rever', 'Sonho Conhecer / Rever')], default=None, max_length=20, null=True, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='local',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Local de Internação'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='local_address',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Endereço do Local de Internação'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='local_name',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Nome do Contato do Local de Internação'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='local_phone',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Telefone do Contato do Local de Internação'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='planning_description',
            field=models.TextField(default=None, null=True, verbose_name='Planejamento do Sonho'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='status',
            field=models.CharField(choices=[('novo', 'Novo'), ('inviavel', 'Inviavel'), ('pre_aprovado', 'Pré-Aprovado')], default='novo', max_length=20, null=True, verbose_name='Status'),
        ),
    ]
