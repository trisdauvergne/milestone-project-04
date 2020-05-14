from django import forms
from .models import DesignerProfile
from django.contrib.auth.models import User
# from allauth.account.forms import SignupForm


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',
                  'email']


# class MyCustomSignupForm(SignupForm):
#     def __init__(self, *args, **kwargs):
#         super(MyCustomSignupForm, self).__init__(*args, **kwargs)
#         self.fields['register_designer'] = forms.BooleanField(required=True)

#     def save(self, request):
#         register_designer = self.cleaned_data.pop('register_designer')
#         ...
#         user = super(MyCustomSignupForm, self).save(request)


class DesignerProfileForm(forms.ModelForm):

    class Meta:
        model = DesignerProfile
        fields = ['first_name',
                  'last_name',
                  'bio',
                  'country']

