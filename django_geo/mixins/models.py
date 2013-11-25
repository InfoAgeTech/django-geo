# -*- coding: utf-8 -*-
from django.db import models

from ..models import Location


class AbstractLocationModelMixin(models.Model):
    """Model mixin for location based models."""
    location = models.ForeignKey(Location,
                                 blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL)

    class Meta:
        abstract = True
