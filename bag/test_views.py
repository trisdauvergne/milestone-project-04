from django.test import TestCase
from prints.models import Print
from profiles.models import RegisteredUserProfile
from django.contrib.auth.models import User


class TestBagViews(TestCase):
    def test_bag_contents(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag_contents.html')

    def test_add_print_to_bag(self):
        # Create a user without specifying an ID
        the_user = User.objects.create()

        # Same for designer. The user field is a FK to an actual user
        the_designer = RegisteredUserProfile.objects.create(
            user=the_user,
            register_as_designer=True,
            register_as_customer=False,
            first_name='test',
            last_name='test',
            bio='test',
            country='US')
        the_print = Print.objects.create(designer=the_designer,
                                         price=25,
                                         image='test.jpg')

        post_data = {
            'quantity': 3,
            'redirect_url': '/bag/'
        }

        response = self.client.post(
            f'/bag/add/{the_print.id}/', post_data)

        session = self.client.session

        # Assert bag is in session
        self.assertTrue(session["bag"])

        print(session["bag"])

        self.assertEqual(session["bag"][str(the_print.id)], 3)

    def test_adjust_bag_quantity(self):
        # Create a user without specifying an ID
        the_user = User.objects.create()

        # Same for designer. The user field is a FK to an actual user
        the_designer = RegisteredUserProfile.objects.create(
            user=the_user,
            register_as_designer=True,
            register_as_customer=False,
            first_name='test',
            last_name='test',
            bio='test',
            country='US')
        the_print = Print.objects.create(designer=the_designer,
                                         price=25,
                                         image='test.jpg')

        post_data = {
            'quantity': 3,
            'redirect_url': '/bag/'
        }

        response = self.client.post(f'/bag/add/{the_print.id}/', post_data)

        session = self.client.session

        post_data = {
            'quantity': 6,
        }

        response = self.client.post(
            f'/bag/adjust/{the_print.id}/', post_data)

        self.assertEqual(session['bag'][f'{the_print.id}'], 6)

        def test_adjust_bag_quantity_to_zero(self):
            # Create a user without specifying an ID
            the_user = User.objects.create()

            # Same for designer. The user field is a FK to an actual user
            the_designer = RegisteredUserProfile.objects.create(
                user=the_user,
                register_as_designer=True,
                register_as_customer=False,
                first_name='test',
                last_name='test',
                bio='test',
                country='US')
            the_print = Print.objects.create(designer=the_designer,
                                             price=25,
                                             image='test.jpg')

            # What is currently in post data
            post_data = {
                'quantity': 3,
                'redirect_url': '/bag/'
            }

            response = self.client.post(f'/bag/add/{the_print.id}/', post_data)

            session = self.client.session

            # New post data
            post_data = {
                'quantity': 0,
            }

            response = self.client.post(
                f'/bag/adjust/{the_print.id}/', post_data)

            # To assume that the bag will be empty
            self.assertNotIn(f'{the_print.id}', session['bag'])
