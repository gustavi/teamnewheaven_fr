# This file is part of Team NewHeaven website.
#
# Team NewHeaven website is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Team NewHeaven website is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Team NewHeaven website. If not, see
# <http://www.gnu.org/licenses/>.

from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(unique=True, max_length=64)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Image(models.Model):

    name = models.CharField(max_length=32)
    image = models.ImageField()
    date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Video(models.Model):

    name = models.CharField(max_length=64)
    key = models.CharField(max_length=16)
    date = models.DateField(auto_now=False)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
