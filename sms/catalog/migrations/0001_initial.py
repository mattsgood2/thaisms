# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-30 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=60)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9)),
                ('image', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('bestselling', models.BooleanField(default=False)),
                ('meta_keywords', models.CharField(max_length=255, verbose_name='Meta Keywords')),
                ('meta_description', models.CharField(max_length=255, verbose_name='Meta Keywords')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'menu',
                'db_table': 'menu',
                'ordering': ['food_name'],
            },
        ),
    ]
