from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class DesignerProfile(models.Model):
    """ A user profile model for designers """
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
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
    email = models.EmailField(max_length=254,
                              null=False,
                              blank=False)

    class Meta:
        verbose_name = 'Designer Profile'

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     """
#     Create or update the user profile
#     """
#     if created:
#         DesignerProfile.objects.create(user=instance)
#     # Existing users: just save the profile
#     instance.designerprofile.save()