# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 07:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passresults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passinout', models.IntegerField(blank=True, null=True)),
                ('passdtday', models.CharField(blank=True, max_length=45, null=True)),
                ('tasktype', models.CharField(blank=True, max_length=50, null=True)),
                ('lastpasstime', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='stuinfo',
            fields=[
                ('userid', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=45, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('classname', models.CharField(blank=True, max_length=45, null=True)),
                ('major', models.CharField(blank=True, max_length=45, null=True)),
                ('department', models.CharField(blank=True, max_length=45, null=True)),
                ('permise', models.CharField(blank=True, max_length=5, null=True)),
                ('fudaoyuanid', models.CharField(blank=True, max_length=45, null=True)),
                ('fudaoyuanname', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timesetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.CharField(blank=True, max_length=45, null=True)),
                ('latetime', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vthdpass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passinout', models.IntegerField(blank=True, null=True)),
                ('passdtday', models.CharField(blank=True, max_length=45, null=True)),
                ('passdttime', models.CharField(blank=True, max_length=45, null=True)),
                ('passdt', models.CharField(blank=True, max_length=90, null=True)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_stay_out_late.stuinfo')),
            ],
        ),
        migrations.AddField(
            model_name='passresults',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_stay_out_late.stuinfo'),
        ),
    ]