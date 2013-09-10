# -*- coding: utf-8 -*-
from django import forms


class LatLongFormMixin(forms.Form):
    """Form mixin for latitute and longitude coordinates."""
    long = forms.FloatField(label='Longitude', required=False)
    lat = forms.FloatField(label='Latitude', required=False)
