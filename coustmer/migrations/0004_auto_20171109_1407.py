# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coustmer', '0003_friendship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zuser',
            name='zhiwei',
        ),
        migrations.AddField(
            model_name='zuser',
            name='faml',
            field=models.CharField(choices=[(0, '女'), (1, '男')], default=0, max_length=4),
        ),
    ]