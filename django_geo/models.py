# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django_geo.managers import LocationManager


class Location(models.Model):
    """Represents a location object.
    
    :param name: the name of the location.
    :param locality: city
    :param subdivision: state
    :param postal_code: zip_code
    :param latitude: latitude of the location
    :param longitude: longitude of the location
    :param ext_source: source of the location information
    :param ext_id: unique identifier for the source of the location information.
    :param category: category (type) of places this is.
    """
    name = models.CharField(max_length=100,
                            blank=True,
                            null=True,
                            verbose_name=_('Name'))
    line1 = models.CharField(max_length=100,
                             blank=True,
                             null=True,
                             verbose_name=_('Address Line 1'))
    line2 = models.CharField(max_length=100,
                             blank=True,
                             null=True,
                             verbose_name=_('Address Line 2'))
    locality = models.CharField(max_length=100,
                                blank=True,
                                null=True,
                                verbose_name=_('City'))
    subdivision = models.CharField(max_length=100,
                                   blank=True,
                                   null=True,
                                   verbose_name=_('State'))
    country = models.CharField(max_length=100,
                               blank=True,
                               null=True,
                               verbose_name=_('Country'))
    postal_code = models.CharField(max_length=100,
                                   blank=True,
                                   null=True,
                                   verbose_name=_('Zip Code'))
    phone = models.CharField(max_length=30,
                             blank=True,
                             null=True,
                             verbose_name=_('Phone'))
    latitude = models.DecimalField(max_digits=10,
                                   decimal_places=5,
                                   blank=True,
                                   null=True)
    longitude = models.DecimalField(max_digits=10,
                                    decimal_places=5,
                                    blank=True,
                                    null=True)
    ext_source = models.CharField(max_length=50, blank=True, null=True)
    ext_id = models.CharField(max_length=50, blank=True, null=True)
    # TODO: is this needed for this model? Restaurant, bar, fitness, etc.
    category = models.CharField(max_length=100, blank=True, null=True)
    objects = LocationManager()


    def get_display(self, exclude_fields=None):
        """Gets the non-html inline location. 
        
        :param exclude_fields: a list of tuple of fields to ignore.  This can
            be any field name on the location object.
        """
        if not exclude_fields:
            exclude_fields = []

        text = u''
        if self.name and 'name' not in exclude_fields:
            text += u'{0}'.format(self.name)

        if self.line1 and 'line1' not in exclude_fields:
            text += u', {0}'.format(self.line1)

        if self.line2 and 'line2' not in exclude_fields:
            text += u', {0}'.format(self.line2)

        city_state_zip = ''

        if self.subdivision and 'subdivision' not in exclude_fields:
            city_state_zip += self.subdivision

        if self.locality and 'locality' not in exclude_fields:
            city_state_zip += u', {0}'.format(self.locality) if city_state_zip else self.locality

        if self.postal_code and 'postal_code' not in exclude_fields:
            city_state_zip += u', {0}'.format(self.postal_code) if city_state_zip else self.postal_code

        if city_state_zip:
            text += u', {0}'.format(city_state_zip)

        if self.country and 'country' not in exclude_fields:
            text += u', {0}'.format(self.country)

        if self.phone and 'phone' not in exclude_fields:
            text += u', {0}'.format(self.phone)

        return text
