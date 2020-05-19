from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the landing 'index' page """

    user = request.user

    # 1. Check if all information.
    # 2. If not, redirect to profile page. 
    return render(request, 'home/index.html')
