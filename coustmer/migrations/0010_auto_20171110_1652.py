# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 08:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coustmer', '0009_auto_20171110_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoucang',
            name='shoucanghua',
            field=models.ManyToManyField(blank=True, null=True, related_name='shoucanghua', to='huati.Hua'),
        ),
        migrations.AlterField(
            model_name='shoucang',
            name='shoucanguser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shoucanguser', to=settings.AUTH_USER_MODEL),
        ),
    ]
