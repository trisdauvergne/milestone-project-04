from django.test import TestCase
# from django.test import Client
# from django.contrib.auth import login
# from django.http import HttpRequest

from django.contrib.auth.models import User
from profiles.models import RegisteredUserProfile

from profiles.forms import RegisteredUserProfileForm

class TestProfilesView(TestCase):
    def test_load_create_profile_page(self):
        # The user
        User.objects.create(username='temporary',
                            email='temp@gmail.com',
                            password='secret')
        # Log the user in
        self.client.login(username='temporary',
                          password='secret')
        # The page, following a redirect
        response = self.client.get('/profiles/create-profile/',
                                   follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='profiles/create_profile.html')

    def test_order_history(self):
        # The user
        User.objects.create(username='temporary',
                            email='temp@gmail.com',
                            password='secret')
        # Log the user in
        self.client.login(username='temporary',
                          password='secret')
        # The page, following a redirect
        response = self.client.get('/profiles/order-history/',
                                   follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='profiles/order_history.html')

    def test_login_user(self):
        """ Check logged in user """
        user = User.objects.create_user(username='temporary',
                                        email='temp@gmail.com',
                                        password='secret')
        login = self.client.login(username='temporary',
                                  email='temp@gmail.com',
                                  password='wrong')
        self.assertFalse(login)

    def test_get_designer_details_in_form(self):
        """ Getting logged in designer's details """
        # Create the user
        the_user = User.objects.create()

        # Create a designer
        the_designer = RegisteredUserProfile.objects.create(user=the_user,
                                                            register_as_designer=True,
                                                            register_as_customer=False,
                                                            first_name='test',
                                                            last_name='test',
                                                            bio='test',
                                                            country='US')

        # The form to show the details
        profile_form = RegisteredUserProfileForm(instance=the_designer)

        # When sent
        self.fail(profile_form.as_p())
