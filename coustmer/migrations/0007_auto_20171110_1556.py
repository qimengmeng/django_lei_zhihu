# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coustmer', '0006_remove_zuser_faml'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caogao',
            name='neirong',
        ),
        migrations.RemoveField(
            model_name='caogao',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='shoucang',
            options={'ordering': ['-id'], 'verbose_name': '收藏', 'verbose_name_plural': '收藏'},
        ),
        migrations.RemoveField(
            model_name='shoucang',
            name='name',
        ),
        migrations.RemoveField(
            model_name='shoucang',
            name='status',
        ),
        migrations.DeleteModel(
            name='Caogao',
        ),
    ]