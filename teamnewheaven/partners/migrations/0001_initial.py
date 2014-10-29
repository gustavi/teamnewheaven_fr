# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(max_length=256, unique=True)),
                ('is_partner', models.BooleanField(default=True, verbose_name='Est un partneaire ? (un ami sinon)')),
                ('description', models.TextField()),
                ('avatar', models.ImageField(upload_to='partners/', blank=True)),
                ('website', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
