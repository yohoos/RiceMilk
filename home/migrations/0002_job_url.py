# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-18 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
