# -*- coding: utf-8 -*-
from django.test import TestCase
from django_geo.models import Location


class NotificationManagerTests(TestCase):

    def test_create_location(self):
        name = 'My Building'
        line1 = '1234 N. Street'
        line2 = 'This building rocks'
        locality = 'Denver'
        subdivision = 'CO'
        country = 'USA'
        postal_code = '12345'
        phone = '(123)-123-1234'
        latitude = -123.42342
        longitude = 34.9876
        ext_source = 'awesomelatandlong.com'
        ext_id = '4321'
        category = 'Food'
        loc = Location.objects.create(latitude=latitude,
                                      longitude=longitude,
                                      name=name,
                                      line1=line1,
                                      line2=line2,
                                      locality=locality,
                                      subdivision=subdivision,
                                      country=country,
                                      postal_code=postal_code,
                                      phone=phone,
                                      ext_source=ext_source,
                                      ext_id=ext_id,
                                      category=category)
        self.assertEqual(name, loc.name)
        self.assertEqual(line1, loc.line1)
        self.assertEqual(line2, loc.line2)
        self.assertEqual(locality, loc.locality)
        self.assertEqual(subdivision, loc.subdivision)
        self.assertEqual(country, loc.country)
        self.assertEqual(postal_code, loc.postal_code)
        self.assertEqual(phone, loc.phone)
        self.assertEqual(latitude, loc.latitude)
        self.assertEqual(longitude, loc.longitude)
        self.assertEqual(ext_source, loc.ext_source)
        self.assertEqual(ext_id, loc.ext_id)
        self.assertEqual(category, loc.category)

    def test_get_display(self):
        """Tests the inline address formatting."""
        name = 'My Building'
        line1 = '1234 N. Street'
        line2 = 'This building rocks'
        locality = 'Denver'
        subdivision = 'CO'
        country = 'USA'
        postal_code = '12345'
        phone = '(123)-123-1234'
        loc = Location.objects.create(name=name,
                                      line1=line1,
                                      line2=line2,
                                      locality=locality,
                                      subdivision=subdivision,
                                      country=country,
                                      postal_code=postal_code,
                                      phone=phone)

        self.assertEqual(loc.get_display(),
                         'My Building, 1234 N. Street, '
                         'This building rocks, '
                         'Denver, CO, 12345, USA, (123)-123-1234')


