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

from django.contrib import admin

from partners.models import Partner


class PartnerAdmin(admin.ModelAdmin):

    list_display = ('name', 'website', 'is_partner')
    list_filter = ('is_partner',)
    ordering = ('name',)
    search_fields = ('name', 'website', 'is_partner')

    prepopulated_fields = {'slug': ('name', ), }

admin.site.register(Partner, PartnerAdmin)
