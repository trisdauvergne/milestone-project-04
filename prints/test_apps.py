from django.test import TestCase
from prints.apps import PrintsConfig
from django.apps import apps


class TestPrintsApps(TestCase):
    def test_prints_apps(self):
        self.assertEqual(PrintsConfig.name, 'prints')
        self.assertEqual(apps.get_app_config('prints').name, 'prints')
