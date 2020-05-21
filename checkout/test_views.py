from django.test import TestCase
from django.conf import settings


# Create your tests here.


class TestCheckoutViews(TestCase):
    
    # def test_save_checkout_data(self):
    #     """ Testing that checkout data is saved """

    def test_checkout_works(self):
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE

        print(stripe_public_key)
        print(stripe_secret_key)