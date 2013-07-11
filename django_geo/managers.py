# -*- coding: utf-8 -*-
from django.db import models


class LocationManager(models.Manager):

    def create(self, latitude=None, longitude=None, **kwargs):

        return super(LocationManager, self).create(latitude=latitude,
                                                   longitude=longitude,
                                                   **kwargs)
