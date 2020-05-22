from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class RegisteredUserProfile(models.Model):
    """ A user profile model for registered users """
    user = models.OneToOneField(User,
                                related_name="user_profile",
                                on_delete=models.CASCADE)
    register_as_designer = models.BooleanField(blank=True)
    register_as_customer = models.BooleanField(blank=True)
    first_name = models.CharField(max_length=30,
                                  null=False,
                                  blank=False)
    last_name = models.CharField(max_length=30,
                                 null=False,
                                 blank=False)
    bio = models.CharField(max_length=240,
                           null=False,
                           blank=False)
    country = CountryField(blank_label='Country',
                           null=False,
                           blank=False)

    class Meta:
        verbose_name = 'Registered User Profile'

    def __str__(self):
        return self.user.username

