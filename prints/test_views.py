from django.test import TestCase
from .models import Print
# from profiles.models import RegisteredUserProfile
# from django.contrib.auth.models import User


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
        the_print = Print.objects.create(designer_id=99,
                                         price=25)
        response = self.client.get(f'/prints/large-print/{the_print.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prints/large_print.html')

    # def test_get_edit_print(self):
    #     the_print = Print.objects.create(designer_id=1,
    #                                      price=25)
    #     response = self.client.get(f'/prints/large-print/{the_print.id}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'prints/large_print.html')
