from django.test import TestCase
from .forms import UploadPrintForm


class TestUploadPrintForm(TestCase):
    """ Testing that the title field is required """
    def test_print_title_is_required(self):
        form = UploadPrintForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    """ Testing that the designer field is not visible in form """
    def test_only_meta_fields_are_displayed(self):
        form = UploadPrintForm()
        self.assertEqual(form.Meta.fields, ['title',
                                            'description',
                                            'size',
                                            'price',
                                            'image'])

