from django.test import TestCase
from .models import Print
from profiles.models import RegisteredUserProfile
from django.contrib.auth.models import User


class TestPrintsView(TestCase):
    def test_get_all_prints(self):
        response = self.client.get('/prints/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prints/all_prints.html')

    def test_get_all_prints_price(self):
        response = self.client.get('/prints/prints-price/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prints/all_prints_price.html')

    def test_get_all_prints_designer(self):
        response = self.client.get('/prints/prints-designer/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prints/all_prints_designer.html')

    def test_get_large_print(self):
        # Create a user without specifying an ID
        the_user = User.objects.create()

        # Same for designer. The user field is a FK to an actual user
        the_designer = RegisteredUserProfile.objects.create(user=the_user,
                                                            register_as_designer=True,
                                                            register_as_customer=False,
                                                            first_name='test',
                                                            last_name='test',
                                                            bio='test',
                                                            country='US')
        the_designer.save()
        # And the designer field here is a FK to an actual designer
        the_print = Print.objects.create(designer=the_designer,
                                         price=25,
                                         image='test.jpg')
        response = self.client.get(f'/prints/large-print/{the_print.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prints/large_print.html')

    def test_get_edit_print(self):
        # The user
        User.objects.create(username='temporary',
                            email='temp@gmail.com',
                            password='secret')
        # Log the user in
        self.client.login(username='temporary',
                          password='secret')
        # Call the user info
        the_user = User.objects.create()
        # Create the designer profile
        the_designer = RegisteredUserProfile.objects.create(user=the_user,
                                                            register_as_designer=True,
                                                            register_as_customer=False,
                                                            first_name='test',
                                                            last_name='test',
                                                            bio='test',
                                                            country='US')
        # Create the print info
        the_print = Print.objects.create(designer=the_designer,
                                         price=25,
                                         image='test.jpg')
        # The page, following a redirect
        response = self.client.get(f'/prints/edit-print/{the_print.id}',
                                   follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='prints/edit_print.html')

    def test_add_print(self):
        # The user
        User.objects.create(username='temporary',
                            email='temporary@gmail.com',
                            password='secret')
        # Logging the user in
        self.client.login(username='temporary',
                          password='secret')
        # The page, following a redirect
        response = self.client.get('/prints/add-print/',
                                   follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='prints/add_print.html')

    def test_delete_print(self):
        # The user
        User.objects.create(username='temporary',
                            email='temporary@gmail.com',
                            password='secret')
        # Logging the user in
        self.client.login(username='temporary',
                          password='secret')
        # The page, following a redirect
        response = self.client.get(f'/prints/delete-print/<print_id>/',
                                   follow=True)
        self.assertEqual(response.status_code, 200)
