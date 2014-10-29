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

import random
import string

from django.db import models

class Email(models.Model):

    address = models.EmailField(max_length=254, unique=True)
    date = models.DateField(auto_now=True)
    key = models.CharField(max_length=64)

    def __str__(self):
        return self.address


def add_in_newsletter(address):
    """
    Add an user in the newsletter.
    """
    try:
        email = Email.objects.get(address=address)
        return 'exist'
    except Email.DoesNotExist:
        email = Email()
        email.address = address
        key = ''.join(
            random.choice(
                string.ascii_lowercase + string.digits
            ) for foo in range(64)
        )
        email.key = key
        email.save()
        return 'success'
