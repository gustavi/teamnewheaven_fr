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

from captcha.models import CaptchaStore

from contact.forms import ContactForm


class ContactTest(TestCase):

    def setUp(self):
        self.client = Client()


    def test_access_contact_page(self):
        """
        Test the access to the contact page. Allow for everybody.
        """
        result = self.client.get('/contact/')
        self.assertEqual(result.status_code, 200)

    def test_valid_form(self):
        """
        Test the contact form.
        """

        # check the captcha store is empty
        captcha_count = CaptchaStore.objects.count()
        self.failUnlessEqual(captcha_count, 0)

        # load the page and check that there's a new captcha objects instances
        for i in range(10):
            result = self.client.get('/contact/')
        captcha_count = CaptchaStore.objects.count()
        self.failUnlessEqual(captcha_count, 10)

        # data for form validation
        first_name = 'First name'
        last_name = 'Last name'
        email = 'email@domain.tld'
        message = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus.
Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed,
dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper
congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est
eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu
massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue.
Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue.
Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed
dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci
luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed
pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales
hendrerit.'''
        newsletter = True
        captcha = CaptchaStore.objects.all()[0]

        form_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'message': message,
            'newsletter': newsletter,
            'captcha_0': captcha.hashkey,
            'captcha_1': captcha.response
        }

        # default form
        form = ContactForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

        # without first name
        data = dict(form_data)
        data['first_name'] = ''
        captcha = CaptchaStore.objects.all()[0]
        data['captcha_0'] = captcha.hashkey
        data['captcha_1'] = captcha.response
        form = ContactForm(data=data)
        self.assertEqual(form.is_valid(), False)

        # without first name
        data = dict(form_data)
        data['last_name'] = ''
        captcha = CaptchaStore.objects.all()[0]
        data['captcha_0'] = captcha.hashkey
        data['captcha_1'] = captcha.response
        form = ContactForm(data=data)
        self.assertEqual(form.is_valid(), False)

        # without first name
        data = dict(form_data)
        data['email'] = ''
        captcha = CaptchaStore.objects.all()[0]
        data['captcha_0'] = captcha.hashkey
        data['captcha_1'] = captcha.response
        form = ContactForm(data=data)
        self.assertEqual(form.is_valid(), False)

        # without message
        data = dict(form_data)
        data['message'] = ''
        captcha = CaptchaStore.objects.all()[0]
        data['captcha_0'] = captcha.hashkey
        data['captcha_1'] = captcha.response
        form = ContactForm(data=data)
        self.assertEqual(form.is_valid(), False)

        # change newsletter to True
        data = dict(form_data)
        data['newsletter'] = True
        captcha = CaptchaStore.objects.all()[0]
        data['captcha_0'] = captcha.hashkey
        data['captcha_1'] = captcha.response
        form = ContactForm(data=data)
        self.assertEqual(form.is_valid(), True)
