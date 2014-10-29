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

from django.test import TestCase
from django.test.client import Client


class DownloadTest(TestCase):

    def setUp(self):
        self.client = Client()


    def test_access_team_page(self):
        """
        Test the access to the team page. Allow for everybody.
        """
        result = self.client.get('/team/')
        self.assertEqual(result.status_code, 200)


    def test_access_team_story_page(self):
        """
        Test the access to the team story page. Allow for everybody.
        """
        result = self.client.get('/team/story/')
        self.assertEqual(result.status_code, 200)
