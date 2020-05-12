from django.shortcuts import render
# from django.contrib.auth.models import User
from profiles.models import DesignerProfile
from django.contrib.auth.models import User

from prints.models import Print


# Create your views here.

def all_designers(request):
    """ A view to return the all designers page """
    all_designers = DesignerProfile.objects.all()

    context = {
        'designers': all_designers,
    }

    return render(request,
                  'designers/all_designers.html',
                  context)


def individual_designer(request, designer_id):
    """ A view to return a page focusing on 1 x designer """
    the_designer = DesignerProfile.objects.get(id=designer_id)
    the_designers_prints = Print.objects.filter(designer_id=the_designer)

    context = {
        'the_designer': the_designer,
        'prints': the_designers_prints,
    }

    return render(request,
                  'designers/individual_designer.html',
                  context)
