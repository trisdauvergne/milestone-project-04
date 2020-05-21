from django.test import TestCase
from .forms import UserForm, RegisteredUserProfileForm

# from allauth.account.forms import SignupForm

# from .models import RegisteredUserProfile


class TestProfilesForms(TestCase):
    """ Testing that password isn't visible in profile form """
    def test_password_not_displayed(self):
        form = UserForm()
        self.assertEqual(form.Meta.fields, ['username',
                                            'email'])

    """ Test that the first name field is required """
    def test_first_name_is_required(self):
        form = RegisteredUserProfileForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
             form.errors['first_name'][0], 'This field is required.')

    """ Test that register as designer isn't required """
    def test_register_as_designer_not_required(self):
        form = RegisteredUserProfileForm({'register_as_designer': False})
        self.assertFalse(form.is_valid())

