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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=32)),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(to='gallery.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('key', models.CharField(max_length=16)),
                ('date', models.DateField()),
                ('category', models.ForeignKey(to='gallery.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
