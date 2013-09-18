# -*- coding: utf-8 -*-
from django.template import Library
from django.template.defaultfilters import safe
from django.utils.html import escape
import urllib

register = Library()

@register.filter
def location_html(location):
    """
    Gets the html for a location object. 
    """

    if not location:
        return u''

    html = u''
    if location.name:
        address = location.get_display(exclude_fields=['phone']).encode('utf-8')
        address = urllib.quote_plus(address)
        url = u'https://maps.google.com/maps?q={0}'.format(address)
        html += u'<a href="{0}" class="name" target="_blank">{1}</a>'.format(url,
                                                                                              escape(location.name))

    if location.line1:
        html += u'<div>{0}</div>'.format(escape(location.line1))

    if location.line2:
        html += u'<div>{0}</div>'.format(escape(location.line2))

    city_state_zip = ''

    if location.subdivision:
        city_state_zip += location.subdivision

    if location.locality:
        city_state_zip += u' {0}'.format(location.locality) if city_state_zip else location.locality

    if location.postal_code:
        city_state_zip += u' {0}'.format(location.postal_code) if city_state_zip else location.postal_code

    if city_state_zip:
        html += u'<div>{0}</div>'.format(escape(city_state_zip))

    if location.country:
        html += u'<div>{0}</div>'.format(escape(location.country))

    if location.phone:
        html += u'<div>{0}</div>'.format(escape(location.phone))

    return safe(u'<address>{0}</address>'.format(html))
