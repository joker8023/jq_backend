# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_stay_out_late', '0002_passresults_passdttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passresults',
            name='lastpasstime',
            field=models.DateTimeField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vthdpass',
            name='passdt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
