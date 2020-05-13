from django.shortcuts import render
# from django.contrib.auth.models import User
from profiles.models import DesignerProfile
from django.contrib.auth.models import User

from prints.models import Print


# Create your views here.

def all_designers(request):
    """ A view to return the all designers page """
    completed_designers = []
    all_designers = DesignerProfile.objects.all()
    for designer in all_designers:
        complete = all([designer.first_name,
                        designer.last_name,
                        designer.bio,
                        designer.country])
        if complete:
            completed_designers.append(designer)
    context = {
        'designers': completed_designers,
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
