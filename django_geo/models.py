# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.gis.db.models.fields import PointField
from django.contrib.gis.geos.point import Point


class Location(models.Model):
    """
    Represents a location object.
    
    :param name: the name of the location.
    :param locality: city
    :param subdivision: state
    :param postal_code: zip_code
    :param latlong: tuple or list of latitude and longitute values. 
        Example: [latitude, longitude] or [38.9401, -94.6807]
    :param category: category (type) of places this is.
    :param source: the source of where the location information was retrieved.
        
    """
    name = models.CharField(max_length=100, required=False,
                            verbose_name=_('Name'))
    line1 = models.CharField(max_length=100, required=False,
                             verbose_name=_('Address Line 1'))
    line2 = models.CharField(max_length=100, required=False,
                             verbose_name=_('Address Line 2'))
    locality = models.CharField(max_length=100, required=False,
                                verbose_name=_('City'))
    subdivision = models.CharField(max_length=100, required=False,
                                   verbose_name=_('State'))
    country = models.CharField(max_length=100, required=False,
                               verbose_name=_('Country'))
    postal_code = models.CharField(max_length=100, required=False,
                                   verbose_name=_('Zip Code'))
    phone = models.CharField(regex=r'^([0-9\(\)\/\+\-]*)', required=False,
                             verbose_name=_('Phone'))
    latlong = PointField(required=False)
    # TODO: is this needed for this model?
    category = models.CharField(required=False)
    source = models.CharField(default='OTHER')


    def __init__(self, latitude=None, longitude=None, *args, **kwargs):
        super(Location, self).__init__(*args, **kwargs)

        if not self.latlong and latitude and longitude:
            # Might not be the right "Point" datatype
            self.latlong = Point(latitude, longitude)

    def get_display(self, exclude_fields=None):
        """
        Gets the non-html inline location. 
        
        :param exclude_fields: a list of tuple of fields to ignore.  This can
            be any field name on the location object.
        """
        if not exclude_fields:
            exclude_fields = []

        html = u''
        if self.name and 'name' not in exclude_fields:
            html += u'{0}'.format(self.name)

        if self.line1 and 'line1' not in exclude_fields:
            html += u', {0}'.format(self.line1)

        if self.line2 and 'line2' not in exclude_fields:
            html += u', {0}'.format(self.line2)

        city_state_zip = ''

        if self.subdivision and 'subdivision' not in exclude_fields:
            city_state_zip += self.subdivision

        if self.locality and 'locality' not in exclude_fields:
            city_state_zip += u', {0}'.format(self.locality) if city_state_zip else self.locality

        if self.postal_code and 'postal_code' not in exclude_fields:
            city_state_zip += u', {0}'.format(self.postal_code) if city_state_zip else self.postal_code

        if city_state_zip:
            html += u', {0}'.format(city_state_zip)

        if self.country and 'country' not in exclude_fields:
            html += u', {0}'.format(self.country)

        if self.phone and 'phone' not in exclude_fields:
            html += u', {0}'.format(self.phone)

        return html
