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


# class CustomSignupForm(SignupForm):
#     first_name = forms.CharField(max_length=30, label='First Name')
#     last_name = forms.CharField(max_length=30, label='Last Name')
#     bio = forms.CharField(max_length=240, label='Your bio')
#     country = forms.CharField(max_length=30, label='Country')

#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.bio = self.cleaned_data['bio']
#         user.country = self.cleaned_data['country']
#         user.save()
#         return user

