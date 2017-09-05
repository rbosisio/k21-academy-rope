# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20170904_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dream',
            name='linked_partners',
        ),
        migrations.AddField(
            model_name='dream',
            name='linked_partners',
            field=models.ManyToManyField(to='api.Partner'),
        ),
        migrations.RemoveField(
            model_name='dream',
            name='linked_volunteers',
        ),
        migrations.AddField(
            model_name='dream',
            name='linked_volunteers',
            field=models.ManyToManyField(to='api.Volunteer'),
        ),
    ]
