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

from django.shortcuts import render

from team.models import Member, Event

month_name = [
    'JANVIER',
    'FÉVRIER',
    'MARS',
    'AVRIL',
    'MAI',
    'JUIN',
    'JUILLET',
    'AOÛT',
    'SEPTEMBRE',
    'OCTOBRE',
    'NOVEMBRE',
    'DÉCEMBRE'
]

def team_list(request):
    """Displays the list of members"""
    
    architects = Member.objects.filter(group__name='Architectes').\
        order_by('name')
    others = Member.objects.filter(group__name='Autres').order_by('name')
    members = Member.objects.all()
    return render(request, 'team/team-list.html', {'members' : members})

def team_member(request, slug):
    """Single page for each member with some informations"""

    member = Member.objects.get(slug=slug)
    return render(request, 'team/team-member.html', {'member' : member })

def team_story(request):
    events_years = []
    years = Event.objects.dates('date', 'year')
    left = True
    for year in years:
        fake_year_start, fake_year_end = False, False
        months = Event.objects.filter(date__year=year.year).dates('date', 'month')
        events_months = []
        for i in range(len(months)):
            fake_event = False
            month = months[i]
            try:
                month_next = months[i+1]
            except IndexError:
                month_next = None
            if month_next:
                if month.month != month_next.month - 1:
                    fake_event = True
            if i == 0 and month.month != 1:
                fake_year_start = True
            if i == len(months)-1 and month.month != 12:
                fake_year_end = True
            events = Event.objects.filter(date__month=month.month, date__year=year.year).values()
            if len(events) == 1:
                for e in events:
                    e['left'] = left
                    e['fake'] = False
                    left = not left
            else:
                events[0]['left'] = True
                events[1]['left'] = False
                events[0]['fake'] = False
                events[1]['fake'] = False
                events = [events[1], events[0]]
            events = list(events)
            if fake_event:
                events[-1]['fake'] = True
            events_months.append(
                {
                    'month': month.month,
                    'month_name': month_name[month.month-1],
                    'events': events,
                }
            )
        events_years.append(
            {
                'year': year.year,
                'months': events_months,
                'fake_start': fake_year_start,
                'fake_end': fake_year_end,
            }
        )
    return render(request, 'team/team-story.html', {'events_years': events_years})
