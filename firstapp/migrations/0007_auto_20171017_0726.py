# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 07:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20171017_0557'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Todo',
        ),
    ]
