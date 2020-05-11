from django import forms

from .models import UploadPrint


class UploadPrintForm(forms.ModelForm):

    class Meta:
        model = UploadPrint
        fields = ['designer',
                  'title',
                  'description',
                  'size',
                  'price',
                  'image']
