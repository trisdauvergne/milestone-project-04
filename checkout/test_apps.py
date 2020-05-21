from django.test import TestCase
from checkout.apps import CheckoutConfig
from django.apps import apps


class TestCheckoutApps(TestCase):
    def test_checkout_apps(self):
        self.assertEqual(CheckoutConfig.name, 'checkout')
        self.assertEqual(apps.get_app_config('checkout').name, 'checkout')
