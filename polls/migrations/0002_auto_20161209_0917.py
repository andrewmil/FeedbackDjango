# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 09:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]