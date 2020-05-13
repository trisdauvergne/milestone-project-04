from django import forms
from .models import DesignerProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',
                #   'first_name',
                #   'last_name',
                  'email']


class DesignerProfileForm(forms.ModelForm):

    class Meta:
        model = DesignerProfile
        fields = ['first_name',
                  'last_name',
                  'bio',
                  'country']

