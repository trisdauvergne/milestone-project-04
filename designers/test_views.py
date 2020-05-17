from django.test import TestCase


class TestPrintsView(TestCase):
    def test_get_all_designers(self):
        response = self.client.get('/designers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'designers/all_designers.html')

    def test_get_all_designers_alphabetical(self):
        response = self.client.get('/designers/designers-alphabetical/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'designers/all_designers_alphabetical.html')
