# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-02 00:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_auto_20180301_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['-date']},
        ),
    ]
