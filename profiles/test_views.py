from django.test import TestCase

from profiles.models import RegisteredUserProfile
from django.contrib.auth.models import User


class TestProfilesView(TestCase):
    def test_create_profile(self):
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
