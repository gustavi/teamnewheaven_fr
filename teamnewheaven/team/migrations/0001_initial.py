# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Team groups',
                'verbose_name': 'Team group',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=256)),
                ('description', models.CharField(max_length=256, blank=True)),
                ('avatar', models.ImageField(upload_to='members/', blank=True)),
                ('website', models.CharField(max_length=256, blank=True)),
                ('twitter', models.CharField(max_length=256, blank=True)),
                ('biography', models.TextField(blank=True)),
                ('group', models.ForeignKey(to='team.Group')),
            ],
            options={
                'verbose_name_plural': 'Team members',
                'verbose_name': 'Team member',
            },
            bases=(models.Model,),
        ),
    ]
