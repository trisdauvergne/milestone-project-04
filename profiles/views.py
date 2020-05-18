from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import RegisteredUserProfile
from checkout.models import Order
from prints.models import Print


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


def order_history(request):
    """ A view for users to see their purchase history """
    user = request.user
    if user.is_authenticated:
            print(user,  '- this is who is signed in')
            customer = get_object_or_404(RegisteredUserProfile, user=user)
            customer_id = customer.id
            print(customer_id, '- The ID of who is logged in')
            all_orders = Order.objects.get(order_number='6A389AA3073B4E8694EB29C834E46B8B')
            print(all_orders, '- testing this specific order')
            all_orders_customer = all_orders.customer.first_name
            print(all_orders_customer, 'but this should be Holli')

    all_orders = Order.objects.all()
    order = all_orders.order_by('-date')
    customer = RegisteredUserProfile.objects.get(user=user)

    context = {
        'user': user,
        'order': order,
        'customer': customer,
    }

    # print(user.id)
    # print(customer.id)
    # print(order.id)
    return render(request,
                  'profiles/order_history.html',
                  context)
