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

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',

    # administration
    url(r'^admin/', include(admin.site.urls)),

    # homepage
    url(r'^$', 'pages.views.homepage', name='homepage'),
    url(r'^team/', include('team.urls')),

    # internal
    url(r'^contact/', include('contact.urls')),
    url(r'^download/', include('download.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^pages/', include('pages.urls')),
    url(r'^partners/', include('partners.urls')),

    # Zinnia blog
    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),

    # Django simple captcha
    url(r'^captcha/', include('captcha.urls')),
)

# Media
urlpatterns += patterns(
    '',
    (
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    )
)

if settings.DEBUG:

    # Static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    # Django Debug Toolbar
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
