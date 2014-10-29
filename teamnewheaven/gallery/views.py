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

from gallery.models import Category, Video, Image


def index(request):
    """
    Displays categories for images and videos.
    """
    cat = Category.objects.all()
    videos = Video.objects.all()
    images = Image.objects.all()
    categories = []
    for c in range(len(cat)):
        categories.append([cat[c], [], []])
        for v in videos:
            if v.category == cat[c]:
                categories[c][1].append(v)
            if len(categories[c][1]) + len(categories[c][2]) > 8:
                break
        for i in images:
            if i.category == cat[c]:
                categories[c][2].append(i)
            if len(categories[c][1]) + len(categories[c][2]) > 8:
                break
    return render(request, 'gallery/index.html', locals())


def single(request, slug):
    """
    Displays all media for a category.
    """
    category = Category.objects.get(slug=slug)
    videos = Video.objects.filter(category=category)
    images = Image.objects.filter(category=category)
    return render(request, 'gallery/single.html', locals())
