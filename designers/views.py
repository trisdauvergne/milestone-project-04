from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def all_designers(request):
    """ A view to return the all designers page """
    all_designers = User.objects.all()
    alphabetical_designers = all_designers.order_by('last_name')

    context = {
        'designers': alphabetical_designers,
    }

    return render(request,
                  'designers/all_designers.html',
                  context)


def individual_designer(request, designer_id):
    """ A view to return a page focusing on 1 x designer """
    the_designer = User.objects.get(id=designer_id)

    context = {
        'the_designer': the_designer,
    }

    return render(request,
                  'designers/individual_designer.html',
                  context)
