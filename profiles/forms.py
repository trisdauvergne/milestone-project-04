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
#         self.fields['is_designer'] = forms.BooleanField(required=True)

#     def save(self, request):
#         is_designer = self.cleaned_data.pop('is_designer')

#         user = super(MyCustomSignupForm, self).save(request)

#         user = super().save(request)
#         if user:
#             User.objects.create(user=user, is_designer=is_designer)
#         return user


class DesignerProfileForm(forms.ModelForm):

    class Meta:
        model = DesignerProfile
        fields = ['first_name',
                  'last_name',
                  'bio',
                  'country']

