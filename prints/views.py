from django.shortcuts import render


def all_prints(request):
    """ A view to return all the prints on the site """

    return render(request,
                  'prints/all_prints.html')
