from django.test import TestCase


class TestBagViews(TestCase):
    def test_bag_contents(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag_contents.html')
