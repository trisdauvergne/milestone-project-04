from django.test import TestCase
from .models import Print
from profiles.models import RegisteredUserProfile
from django.contrib.auth.models import User


class TestPrintModels(TestCase):

    def test_print_model_fields(self):
        the_user = User.objects.create()
        the_designer = RegisteredUserProfile.objects.create(
            user=the_user,
            register_as_designer=True,
            register_as_customer=False,
            first_name='test',
            last_name='test',
            bio='test',
            country='US')
        the_print = Print.objects.create(designer=the_designer,
                                         title='test',
                                         description='test',
                                         size='test',
                                         price=25,
                                         image='test.jpg')
        self.assertTrue(the_print)
