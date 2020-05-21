from django.test import TestCase
from home.apps import HomeConfig
from django.apps import apps


class TestHomeApps(TestCase):
    def test_home_apps(self):
        self.assertEqual(HomeConfig.name, 'home')
        self.assertEqual(apps.get_app_config('home').name, 'home')
