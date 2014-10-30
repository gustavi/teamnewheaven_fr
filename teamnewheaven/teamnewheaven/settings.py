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

"""
Django settings for teamnewheaven project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'txzhe&fx7+(370k79wgtpi#1$%z-*@e70#06#+o_tn&y4i4c63'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # Internal
    'contact',
    'pages',
    'team',
    'download',
    'gallery',
    'newsletter',
    'partners',
    # External
    'debug_toolbar.apps.DebugToolbarConfig',
    'django_comments',
    'tagging',
    'mptt',
    'zinnia_foundation',
    'zinnia',
    'captcha',
    'easy_thumbnails',
    'raven.contrib.django.raven_compat',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware', # in first
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS =  (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    # third apps
    'zinnia.context_processors.version',
    'dealer.contrib.django.context_processor',
    'pages.context_processors.global_settings',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

ROOT_URLCONF = 'teamnewheaven.urls'

WSGI_APPLICATION = 'teamnewheaven.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

gettext = lambda x: x

LANGUAGES = (
   ('fr', gettext('Français')),
   ('en', gettext('Anglais')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Templates files for all apps

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


# Medias

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Others settings

SITE_ID = 2

APPEND_SLASH = True


# Django Simple Captcha Configuration

CAPTCHA_FONT_SIZE = 34
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_LENGTH = 6
CAPTCHA_NOISE_FUNCTIONS = (
    'captcha.helpers.noise_arcs',
    'captcha.helpers.noise_dots'
)
CAPTCHA_LETTER_ROTATION = (-20, 20)


# Zinnia

ZINNIA_MARKUP_LANGUAGE = 'markdown'


# Easy thumbnail

THUMBNAIL_ALIASES = {
    '': {
        'member_avatar': {
            'size' : (250, 250),
            'crop' : True,
            'quality' : 100,
        },
        'member_avatar_big': {
            'size' : (500, 500),
            'crop' : True,
            'quality' : 100,
        },
        'video_homepage': {
            'size' : (250, 250),
            'crop' : True,
            'quality' : 100,
        },
        'friend_avatar': {
            'size' : (250, 250),
            'quality' : 100,
        },
        'gallery_index': {
            'size' : (480, 360),
            'quality' : 100,
            'crop' : True,
        },
    },
}


# Django Debug Toolbar
# http://django-debug-toolbar.readthedocs.org

DEBUG_TOOLBAR_PATCH_SETTINGS = False # not adjust settings automatically


# Dealer
# https://github.com/klen/dealer#django-support

DEALER_TYPE = 'git'
DEALER_PATH = BASE_DIR


# TNH settings

GOOGLE_ANALYTICS = None
TNH = {
    'forum': {
        'url': 'http://forum.teamnewheaven.fr/',
        'application': 'http://forum.teamnewheaven.fr/viewforum.php?id=3',
    }
}

try:
    from teamnewheaven.settings_prod import *
except ImportError:
    pass
