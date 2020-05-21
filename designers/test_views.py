from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import RegisteredUserProfile


class TestDesignersView(TestCase):
    def test_get_all_designers(self):
        response = self.client.get('/designers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'designers/all_designers.html')

    def test_get_all_designers_alphabetical(self):
        response = self.client.get('/designers/designers-alphabetical/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'designers/all_designers_alphabetical.html')

    def test_get_individual_designer(self):
        # Create a user
        the_user = User.objects.create()

        # Create the designer
        the_designer = RegisteredUserProfile.objects.create(
            user=the_user,
            register_as_designer=True,
            register_as_customer=False,
            first_name='test',
            last_name='test',
            bio='test',
            country='US')

        response = self.client.get(
            f'/designers/designer-detail/{the_designer.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'designers/individual_designer.html')
