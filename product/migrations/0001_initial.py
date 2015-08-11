# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('visible', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'carousel/')),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('show_on_home_page', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'category banners',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('price', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=255, null=True)),
                ('manufacturer', models.CharField(max_length=255, null=True)),
                ('brand', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(null=True, upload_to=b'products/', blank=True)),
                ('popularity', models.IntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('visible', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='product.Category')),
            ],
            options={
                'verbose_name_plural': 'products',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='banners',
            field=models.ManyToManyField(to='product.CategoryBanner'),
        ),
    ]
