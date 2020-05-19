from django.test import TestCase
from .models import RegisteredUserProfile
from django.contrib.auth.models import User


class TestProfilesModel(TestCase):

    def test_profiles_model_fields(self):
        the_user = User.objects.create()
        the_registered_user = RegisteredUserProfile.objects.create(user=the_user,
                                                                   register_as_designer=True,
                                                                   register_as_customer=False,
                                                                   first_name='test',
                                                                   last_name='test',
                                                                   bio='test',
                                                                   country='US')
        self.assertTrue(the_registered_user)
