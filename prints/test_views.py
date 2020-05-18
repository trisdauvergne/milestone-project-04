from django.test import TestCase
from .models import Print
from profiles.models import RegisteredUserProfile
from django.contrib.auth.models import User


class TestPrintsView(TestCase):
    # def test_get_all_prints(self):
    #     response = self.client.get('/prints/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'prints/all_prints.html')

    # def test_get_all_prints_price(self):
    #     response = self.client.get('/prints/prints-price/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'prints/all_prints_price.html')

    # def test_get_all_prints_designer(self):
    #     response = self.client.get('/prints/prints-designer/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'prints/all_prints_designer.html')

    def test_get_large_print(self):
    # Create the user w/o specifying the id. Django will give it one
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

    # def test_get_edit_print(self):
    #     # Create the user w/o specifying the id. Django will give it one
    #     the_user = User.objects.create()
    #     # Same for designer. The user field is a FK to an actual user
    #     the_designer = RegisteredUserProfile.objects.create(user=the_user,
    #                                                         register_as_designer=True,
    #                                                         register_as_customer=False,
    #                                                         first_name='test',
    #                                                         last_name='test',
    #                                                         bio='test',
    #                                                         country='US')
    #     # And the designer field here is a FK to an actual designer
    #     the_print = Print.objects.create(designer=the_designer,
    #                                         price=25,
    #                                         image='test.jpg')
        
    #     response = self.client.get(f'/prints/edit-print/{the_print.id}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'prints/edit_print.html') 

    # def test_add_print(self):
    #     response = self.client.get('/prints/add-print/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'prints/add_print.html')
