from django.shortcuts import render
from prints.models import Print

import random

# Create your views here.


def index(request):
    """ A view to return the landing 'index' page """

    background_prints = Print.objects.all()
    random_print = random.choice(background_prints)

    context = {
        'print': random_print,
    }

    return render(request,
                  'home/index.html',
                  context)
