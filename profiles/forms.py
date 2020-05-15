from django import forms
from .models import RegisteredUserProfile
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',
                  'email']


class RegisteredUserProfileForm(forms.ModelForm):

    class Meta:
        model = RegisteredUserProfile
        fields = ['first_name',
                  'last_name',
                  'bio',
                  'country']


class UserRegistrationType(SignupForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationType, self).__init__(*args, **kwargs)
        self.fields['register_as_designer'] = forms.BooleanField(required=False)
        self.fields['register_as_customer'] = forms.BooleanField(required=False)

    def save(self, request):
        register_as_designer = self.cleaned_data.pop('register_as_designer')
        register_as_customer = self.cleaned_data.pop('register_as_customer')

        user = super().save(request)

        if user:
            RegisteredUserProfile.objects.create(user=user,
                                                 register_as_designer=register_as_designer,
                                                 register_as_customer=register_as_customer)
        return user
