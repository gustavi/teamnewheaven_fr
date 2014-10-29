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

from datetime import datetime
import unicodedata

from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

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
            send = True
            name = str(data['first_name']) + ' ' + str(data['last_name'])
            email = str(data['email'])
            message = unicodedata.normalize('NFKD', data['message']).encode('ascii','ignore')
            mail_content = 'Vous venez de recevoir un message via le formulaire de contact sur teamnewheaven.fr.<br/>----------<br/>Envoyé le '
            mail_content += str(datetime.now())
            mail_content += ' par '
            mail_content += name
            mail_content += ' (<a href="mailto:'
            mail_content += email
            mail_content += '">'
            mail_content += email
            mail_content += '</a>).<br/>----------<br/>Message : <br/><p style="white-space: pre-line">'
            mail_content += message
            mail_content += '</p><br/>----------<br/>IP : '
            mail_content += str(request.META['REMOTE_ADDR'])
            mail_content += '.'
            msg = EmailMultiAlternatives('Contact teamnewheaven.fr - ' + name, mail_content, 'contact@teamnewheaven.fr', settings.CONTACT_EMAIL)
            msg.attach_alternative(mail_content, "text/html")
            msg.send()
    else:
        form = ContactForm()

    return render(request, 'contact/contact-index.html', {'form' : form, 'send' : send})
