from django.shortcuts import render, redirect
# from django.contrib.auth.models import User

from .forms import DesignerProfileForm


def create_profile(request):
    """ A view to render a page where users can create a profile """
    form = DesignerProfileForm()
    if request.method == 'POST':
        form = DesignerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_designers')
    else:
        form = DesignerProfileForm()
    return render(request,
                  'profiles/create_profile.html',
                  {'form': form})
