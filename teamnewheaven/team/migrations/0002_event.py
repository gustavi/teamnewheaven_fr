# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('typ', models.CharField(max_length=3, choices=[('MEM', 'Nouveau membre'), ('VID', 'Vidéo'), ('EVT', 'Événement'), ('AUT', 'Autre')])),
                ('description', models.CharField(max_length=256, blank=True)),
                ('link', models.URLField(max_length=256, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Team members',
                'verbose_name': 'Team member',
            },
            bases=(models.Model,),
        ),
    ]
