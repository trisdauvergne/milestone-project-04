from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.

class TestCheckoutViews(TestCase):

    # def test_save_checkout_data(self):
    
    def test_checkout_page(self):
        order_number = 'D608177B290B4E0497576EF75047E68E'
        response = self.client.get('/checkout/checkout-success/D608177B290B4E0497576EF75047E68E/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')



    # def test_checkout_success_page(self):
    