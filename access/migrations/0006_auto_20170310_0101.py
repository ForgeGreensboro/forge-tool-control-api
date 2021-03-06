# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 01:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0005_auto_20170305_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logentry',
            name='user',
        ),
        migrations.AddField(
            model_name='logentry',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='logEntries', to='access.Profile'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logEntries', to='access.Machine'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='machine_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='profile',
            name='member_card_id',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
