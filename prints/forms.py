from django import forms

from .models import Print


class UploadPrintForm(forms.ModelForm):

    class Meta:
        model = Print
        fields = ['designer',
                  'title',
                  'description',
                  'size',
                  'price',
                  'image']
