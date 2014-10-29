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

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.http import require_POST

from newsletter.models import add_in_newsletter, Email


@require_POST
def subscribe(request):
    """
    """
    response = 'fail'
    try:
        address = request.POST['email']
    except:
        address = None
    if address:
        response = add_in_newsletter(address)
    return HttpResponse(response)


def unsubscribe(request, key):
    """
    Manage his email address.
    """
    try:
        Email.objects.get(key=key)
    except Email.DoesNotExist:
        return Http404
    return render(request, 'newsletter/management.html', {})
