from django import forms
from .models import DesignerProfile


class DesignerProfileForm(forms.ModelForm):

    class Meta:
        model = DesignerProfile
        fields = ['user',
                  'first_name',
                  'last_name',
                  'bio',
                  'country',
                  'email']


