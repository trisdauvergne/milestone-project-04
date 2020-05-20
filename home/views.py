from django.shortcuts import render
from prints.models import Print

import random

# Create your views here.


def index(request):
    """ A view to return the landing 'index' page """

    # user = request.user

    background_prints = Print.objects.all()
    random_print = random.choice(background_prints)

    context = {
        'print': random_print,
    }

    # 1. Check if all information.
    # 2. If not, redirect to profile page.
    return render(request,
                  'home/index.html',
                  context)
