# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_report_http_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='作成日時'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='最終更新日時'),
        ),
    ]