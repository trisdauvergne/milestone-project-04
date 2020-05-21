from django.test import TestCase
from bag.apps import BagConfig
from django.apps import apps


class TestBagApps(TestCase):
    def test_bag_apps(self):
        self.assertEqual(BagConfig.name, 'bag')
        self.assertEqual(apps.get_app_config('bag').name, 'bag')
