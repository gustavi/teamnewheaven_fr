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

from django.contrib import admin

from team.models import Member, Group, Event

class GroupAdmin(admin.ModelAdmin):

    list_display   = ('name',)
    list_filter    = ('name',)

class MemberAdmin(admin.ModelAdmin):

    list_display   = ('name', 'group', 'website', 'twitter',)
    list_filter    = ('group',)
    ordering       = ('name',)
    search_fields  = ('name', 'website', 'twitter', 'group')
    
    fieldsets = (
        ('Main', {
            'fields': ('name', 'group', 'slug')
        }),
        ('Avatar', {
            'description' : 'Mettre si possible la même largeur et la même longueur. Il est conseillé de mettre une image entre 200*200px et 400*400px',
            'fields' : ('avatar',)
        }),
        ('Links', {
            'description' : 'Pour Twitter, ne pas inclure le « @ ».',
            'fields' : ('website', 'twitter')
        }),
        ('Description and bio', {
            'description' : 'Mettre seulement quelques mots présentant le rôle dans « Description » (exemple : « Architecte »), la biographie est là pour le reste.',
            'fields' : ('description', 'biography')
        }),
    )
    
    prepopulated_fields = {'slug': ('name', ), }

admin.site.register(Group, GroupAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Event)
