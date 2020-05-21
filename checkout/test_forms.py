from django.test import TestCase
from django.conf import settings
from checkout.forms import OrderForm


# Create your tests here.


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

    # def test_placeholders_in_form(self):
    #     form = OrderForm()
        # fields = ('full_name',
        #           'email',
        #           'phone_number',
        #           'street_address_1',
        #           'street_address_2',
        #           'town',
        #           'country',
        #           'postcode')
        # placeholders = {
        #     'full_name': 'Full Name',
        #     'email': 'Email Address',
        #     'phone_number': 'Phone Number',
        #     'street_address_1': 'Address 1',
        #     'street_address_2': 'Address 2',
        #     'town': 'Town / City',
        #     'country': 'Country',
        #     'postcode': 'Postal Code',
        # }
        # for field in self.fields:
        #     if self.fields[field].required:
        #         placeholder = f'{placeholders[field]} *'
        #     else:
        #         placeholder = placeholders[field]
        #     self.fields[field].widget.attrs['placeholder'] = placeholder
        # self.assertTrue(form.fields['full_name': 'Full Name',
        #                             'email': 'Email Address',
        #                             'phone_number': 'Phone Number',
        #                             'street_address_1': 'Address 1',
        #                             'street_address_2': 'Address 2',
        #                             'town': 'Town / City',
        #                             'country': 'Country',
        #                             'postcode': 'Postal Code', ])




# class TestProfilesForms(TestCase):
#     """ Testing that password isn't visible in profile form """
#     def test_password_not_displayed(self):
#         form = UserForm()
#         self.assertEqual(form.Meta.fields, ['username',
#                                             'email'])

#     """ Test that the first name field is required """
#     def test_first_name_is_required(self):
#         form = RegisteredUserProfileForm({'first_name': ''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('first_name', form.errors.keys())
#         self.assertEqual(form.errors['first_name'][0],
#                                      'This field is required.')

#     """ Test that register as designer isn't required """
#     def test_register_as_designer_not_required(self):
#         form = RegisteredUserProfileForm({'register_as_designer': False})
#         self.assertFalse(form.is_valid())