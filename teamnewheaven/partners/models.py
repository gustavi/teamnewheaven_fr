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

class Partner(models.Model):

    """All members in the team."""

    name = models.CharField(unique=True, max_length=64)
    slug = models.SlugField(unique=True, max_length=256)
    is_partner = models.BooleanField(
        'Est un partneaire ? (un ami sinon)',
        default=True
    )
    description = models.TextField()
    avatar = models.ImageField(blank=True, upload_to='partners/')
    website = models.CharField(max_length=256)

    def __str__(self):
        return self.name
