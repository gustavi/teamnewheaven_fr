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

from django.shortcuts import render

from gallery.models import Video


def homepage(request):
    """
    Homepage with last informations (news, videos...) and links.
    """
    videos = Video.objects.order_by('-date')[:4]

    return render(request, 'pages/index.html', locals())


def legals(request):
    """
    Legals notice page.
    """
    return render(request, 'pages/legals.html', {})


def about(request):
    """
    About page.
    """
    return render(request, 'pages/about.html', {})
