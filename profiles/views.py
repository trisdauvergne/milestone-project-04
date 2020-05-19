from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import RegisteredUserProfile
from checkout.models import Order, OrderLineItem

from .forms import RegisteredUserProfileForm, UserForm


@login_required
def create_profile(request):
    """ A view to render a page where users can create a profile """

    user = request.user

    user_form = UserForm(instance=user)

    designer = get_object_or_404(RegisteredUserProfile,
                                 user=user)

    designer_profile_form = RegisteredUserProfileForm(instance=designer)

    if request.method == 'POST':

        user_form = UserForm(request.POST,
                             instance=user)
        designer_profile_form = RegisteredUserProfileForm(request.POST,
                                                          instance=designer)

        if user_form.is_valid():
            user_form.save()

        if designer_profile_form.is_valid():
            designer_profile_form.save()

    return render(request,
                  'profiles/create_profile.html',
                  {'user_form': user_form,
                   'designer_form': designer_profile_form})


@login_required
def order_history(request):
    """ A view for users to see their purchase history """
    # Get the logged in user
    user = request.user
    the_user = get_object_or_404(RegisteredUserProfile, user=user)

    # Get the logged in user's orders
    the_users_orders = Order.objects.filter(customer=the_user)

    # Get the line items from the order
    line_items = OrderLineItem.objects.all()

    context = {
        'orders': the_users_orders,
        # 'line_items': line_items,
    }

    return render(request,
                  'profiles/order_history.html',
                  context)

