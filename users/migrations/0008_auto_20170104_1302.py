# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170103_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Picture',
            field=models.ImageField(null=True, upload_to=b'lab6/users/static/css/'),
        ),
    ]
