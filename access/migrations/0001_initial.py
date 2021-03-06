# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 00:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Access_Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('entry_type', models.CharField(choices=[('AR', 'Access Reqeust'), ('AG', 'Access Granted'), ('ADL', 'Access Denied Access Level'), ('ADR', 'Access Denied Reservation'), ('ADM', 'Access Denied Membership')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_address', models.CharField(max_length=15)),
                ('machine_name', models.CharField(max_length=50)),
                ('access_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='access.Access_Level')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='access.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_membership', models.BooleanField()),
                ('department_head', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='access.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='access.Machine')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='logentry',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='access.Machine'),
        ),
        migrations.AddField(
            model_name='logentry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logEntry', to=settings.AUTH_USER_MODEL),
        ),
    ]
