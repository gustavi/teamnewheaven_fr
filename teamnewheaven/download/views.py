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

import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from download.models import Item


def index(request):
    """
    Display all downloads files.
    """
    items = Item.objects.all()
    month = datetime.date.today() - datetime.timedelta(days=30)
    return render(request, 'download/download_index.html', locals())


def download(request, pk):
    """
    Download a single file.
    """
    item = get_object_or_404(Item, pk=pk)
    item.downloads += 1
    item.save()
    return HttpResponseRedirect(item.get_file_url())
