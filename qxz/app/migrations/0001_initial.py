# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qxz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
		('name', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
    ]
