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

from datetime import datetime

from django.shortcuts import render

from contact.forms import ContactForm
from contact.models import Contact


def index(request):
    """Contact form"""

    send = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.data
            contact = Contact()
            contact.first_name = data['first_name']
            contact.last_name = data['last_name']
            contact.email = data['email']
            contact.message = data['message']
            contact.date = datetime.now()
            contact.ip = request.META['REMOTE_ADDR']
            contact.save()
    else:
        form = ContactForm()

    return render(
        request,
        'contact/contact-index.html',
        {'form': form, 'send': send}
    )
