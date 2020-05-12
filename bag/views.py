from django.shortcuts import render, redirect

# Create your views here.


def bag_contents(request):
    """ A view that displays the contents of the shopping bag """
    return render(request,
                  'bag/bag_contents.html')


def add_print_to_bag(request, print_id):
    """ Add a print to the bag with a specified quantity """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if print_id in list(bag.keys()):
        bag[print_id] += quantity
    else:
        bag[print_id] = quantity

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)
