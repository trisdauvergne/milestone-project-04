from django.test import TestCase
from designers.apps import DesignersConfig
from django.apps import apps


class TestDesignerstApps(TestCase):
    def test_designer_apps(self):
        self.assertEqual(DesignersConfig.name, 'designers')
        self.assertEqual(apps.get_app_config('designers').name, 'designers')
