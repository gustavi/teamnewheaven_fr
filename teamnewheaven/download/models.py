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

from teamnewheaven import settings

class Liste(models.Model):

    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Item(models.Model):

    name = models.CharField(max_length=32)
    item = models.FileField(upload_to='files/%Y/%m/%d')
    downloads = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)
    liste = models.ForeignKey(Liste)

    def __str__(self):
        return self.name

    def get_link_url(self):
        return '/download/file/{}/'.format(self.pk)

    def get_file_url(self):
        return settings.MEDIA_URL + str(self.item)
