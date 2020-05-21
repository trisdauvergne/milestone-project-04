from django.test import TestCase
from profiles.apps import ProfilesConfig
from django.apps import apps


class TestProfilesApps(TestCase):
    def test_profiles_apps(self):
        self.assertEqual(ProfilesConfig.name, 'profiles')
        self.assertEqual(apps.get_app_config('profiles').name, 'profiles')
