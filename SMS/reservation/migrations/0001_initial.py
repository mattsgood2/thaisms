# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-29 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mobile_number', models.CharField(max_length=15)),
                ('party_size', models.CharField(max_length=10)),
                ('comments', models.TextField(max_length=255)),
                ('time', models.DateTimeField()),
                ('time_zone', timezone_field.fields.TimeZoneField(default='GB')),
                ('task_id', models.CharField(blank=True, editable=False, max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
