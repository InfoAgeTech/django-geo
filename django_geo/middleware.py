# -*- coding: utf-8 -*-
from django.utils import timezone


class TimezoneMiddleware(object):
    """Middleware to get a users timezone if one exists.  That way datetime can
    always be displayed according to either the users preferred setting or
    the browser's setting.

    @see: https://docs.djangoproject.com/en/dev/topics/i18n/timezones/#selecting-the-current-time-zone
    """
    def process_request(self, request):
        tz = request.session.get('user_timezone')

        if tz:
            timezone.activate(tz)
        else:
            timezone.deactivate()