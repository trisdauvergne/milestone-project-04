from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from prints.models import Print


def bag_contents(request):

    bag_items = []
    total = 0
    print_quantity = 0
    bag = request.session.get('bag', {})

    for print_id, quantity in bag.items():
        print = get_object_or_404(Print, id=print_id)
        total += quantity * print.price
        print_quantity += quantity
        bag_items.append({
            'print_id': print_id,
            'quantity': quantity,
            'print': print,
        })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'print_quantity': print_quantity,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
