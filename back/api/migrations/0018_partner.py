# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20170901_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='Nome')),
                ('document_type', models.CharField(choices=[('pf', 'Pessoa Física'), ('pj', 'Pessoa Jurídica')], max_length=20, verbose_name='Opção de pessoa')),
                ('contact_name', models.CharField(default=None, max_length=255, null=True, verbose_name='Nome do contato')),
                ('document', models.CharField(default=None, max_length=255, null=True, verbose_name='Documento')),
                ('telephone', models.CharField(default=None, max_length=255, verbose_name='Telefone')),
                ('cellphone', models.CharField(default=None, max_length=255, verbose_name='Celular')),
                ('address', models.CharField(default=None, max_length=255, verbose_name='Endereço ')),
                ('has_specific_dream', models.BooleanField(default=False, verbose_name='Tem sonho específico?')),
                ('money_help', models.BooleanField(default=False, verbose_name='Ajuda com dinheiro?')),
                ('service_help', models.BooleanField(default=False, verbose_name='Ajuda com seviço?')),
                ('help_description', models.TextField(default=None, verbose_name='Descrição da ajuda')),
                ('observation', models.TextField(default=None, verbose_name='Observações (Especificar doação)')),
                ('status', models.CharField(choices=[('novo', 'Novo'), ('aprovado', 'Aprovado'), ('reprovado', 'Reprovado')], default=None, max_length=20, verbose_name='Designação do voluntário ')),
                ('available_days_times', models.ManyToManyField(to='api.AvailableDaysTimes')),
            ],
        ),
    ]
