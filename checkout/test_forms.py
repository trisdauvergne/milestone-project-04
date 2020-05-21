from django.test import TestCase
from checkout.forms import OrderForm


class TestCheckoutForms(TestCase):

    def test_checkout_order_form_fields(self):
        """ Checking the form Meta fields """
        form = OrderForm()
        self.assertTrue(form.Meta.fields, ['full_name',
                                           'email',
                                           'phone_number',
                                           'street_address_1',
                                           'street_address_2',
                                           'town',
                                           'country',
                                           'postcode'])

    def test_checkout_order_form_autofocus_full_name(self):
        """ Check automatic focus on full_name """
        form = OrderForm()
        self.assertTrue(form.fields['full_name'].widget.attrs['autofocus'])
