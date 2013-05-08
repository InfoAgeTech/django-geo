# -*- coding: utf-8 -*-
from django.contrib.gis.db import models


class LocationManager(models.GeoManager):

    def create(self, latitude=None, longitude=None, **kwargs):

        return super(LocationManager, self).create(latitude=latitude,
                                                   longitude=longitude,
                                                   **kwargs)
