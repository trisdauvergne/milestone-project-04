from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import DesignerProfile

from .forms import DesignerProfileForm, UserForm


@login_required
def create_profile(request):
    """ A view to render a page where users can create a profile """

    user = request.user

    user_form = UserForm(instance=user)

    designer = get_object_or_404(DesignerProfile,
                                 user=user)

    designer_profile_form = DesignerProfileForm(instance=designer)

    if request.method == 'POST':

        user_form = UserForm(request.POST,
                             instance=user)
        designer_profile_form = DesignerProfileForm(request.POST,
                                                    instance=designer)

        if user_form.is_valid():
            user_form.save()

        if designer_profile_form.is_valid():
            designer_profile_form.save()

    return render(request,
                  'profiles/create_profile.html',
                  {'user_form': user_form,
                   'designer_form': designer_profile_form})
