# coding: utf-8
#
# This file is part of Team NewHeaven website.
#
# Team NewHeaven website is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Team NewHeaven website is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Team NewHeaven website. If not, see <http://www.gnu.org/licenses/>.

from django.db import models

class Group(models.Model):

    """Groups for members list"""

    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team group'
        verbose_name_plural = 'Team groups'


class Member(models.Model):

    """All members in the team."""

    name = models.CharField(unique=True, max_length=64)
    slug = models.SlugField(unique=True, max_length=256)
    group = models.ForeignKey('Group')
    description = models.CharField(max_length=256, blank=True)
    avatar = models.ImageField(blank=True, upload_to='members/')
    website = models.CharField(max_length=256, blank=True)
    twitter = models.CharField(max_length=256, blank=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team member'
        verbose_name_plural = 'Team members'


class Event(models.Model):

    """All members in the team."""

    TYP_CHOICES = (
        ('MEM', 'Nouveau membre'),
        ('VID', 'Vidéo'),
        ('EVT', 'Événement'),
        ('AUT', 'Autre'),
    )

    name = models.CharField(unique=True, max_length=64)
    typ = models.CharField(max_length=3, choices=TYP_CHOICES)
    description = models.TextField()
    link = models.URLField(max_length=256, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
