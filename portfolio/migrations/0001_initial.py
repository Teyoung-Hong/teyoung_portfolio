# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-18 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='タイトル')),
                ('section', models.CharField(choices=[('skills', 'skills'), ('works', 'works'), ('coming', 'coming')], default='coming', max_length=255, verbose_name='セクション')),
                ('genre', models.CharField(choices=[('laguages', 'languages'), ('programming', 'programming'), ('else', 'else')], default='else', max_length=255, verbose_name='ジャンル')),
                ('subTitle', models.CharField(default='タイトル欄', max_length=255, verbose_name='名目')),
                ('desc', models.CharField(default='説明が入ります', max_length=255, verbose_name='説明')),
            ],
        ),
    ]
