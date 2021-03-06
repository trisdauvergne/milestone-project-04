from django.shortcuts import render, redirect, reverse
from django.contrib import messages
# from prints.models import Print


def bag_contents(request):
    """ A view that displays the contents of the shopping bag """
    return render(request,
                  'bag/bag_contents.html')


def add_print_to_bag(request, print_id):
    """ Add a print to the bag with a specified quantity """

    # the_print = Print.objects.get(id=print_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if print_id in list(bag.keys()):
        bag[print_id] += quantity
        print('test print')
        messages.success(request, f'The print was added to your bag!')
    else:
        bag[print_id] = quantity

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
    messages.success(request, f'Your print was removed from Plan Chest')

    # The bag being updated
    request.session['bag'] = bag

    return redirect(reverse('bag_contents'))
