import unittest

from geopoliticalzones import zones


class MyTestCase(unittest.TestCase):
    def test_that_zone_exist(self):
        self.nigeria_zones = zones
    def test_that_zone_is(self):
        self.nigeria_zones = zones
        self.assertEqual( zones.NORTH_CENTRAL, self.nigeria_zones.get_state("Kogi", zones))
