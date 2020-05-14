from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from prints.models import Print

# Create your views here.


def bag_contents(request):
    """ A view that displays the contents of the shopping bag """
    return render(request,
                  'bag/bag_contents.html')


def add_print_to_bag(request, print_id):
    """ Add a print to the bag with a specified quantity """

    the_print = Print.objects.get(id=print_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if print_id in list(bag.keys()):
        bag[print_id] += quantity
    else:
        bag[print_id] = quantity
        # messages.success(request, f'Added to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag_quantity(request, print_id):
    """ Adjust the quantity of a print in the bag """
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[print_id] = quantity
    else:
        del bag[print_id]

    request.session['bag'] = bag
    return redirect(reverse('bag_contents'))


def remove_print(request, print_id):
    """ Remove prints from the shopping bag """
    # Get the bag information
    bag = request.session.get('bag', {})

    # Action, to remove the item
    del bag[print_id]

    # The bag being updated
    request.session['bag'] = bag

    return redirect(reverse('bag_contents'))
