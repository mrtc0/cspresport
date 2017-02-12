# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-12 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_uri', models.URLField(blank=True, verbose_name='document-uri')),
                ('referrer', models.CharField(blank=True, max_length=250, verbose_name='referrer')),
                ('blocked_uri', models.URLField(blank=True, verbose_name='blocked-uri')),
                ('effective_directive', models.CharField(blank=True, max_length=250, verbose_name='effectiveDirective')),
                ('violated_directive', models.CharField(blank=True, max_length=250, verbose_name='violatedDirective')),
                ('original_policy', models.CharField(blank=True, max_length=250, verbose_name='originalPolicy')),
                ('disposition', models.CharField(blank=True, max_length=250, verbose_name='disposition')),
                ('source_file', models.CharField(blank=True, max_length=250, verbose_name='sourceFile')),
                ('status_code', models.CharField(blank=True, max_length=250, verbose_name='statusCode')),
                ('line_number', models.CharField(blank=True, max_length=250, verbose_name='lineNumber')),
                ('column_number', models.CharField(blank=True, max_length=250, verbose_name='columnNumber')),
            ],
        ),
    ]
