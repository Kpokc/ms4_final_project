from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import *


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'total': total,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                if size == "small":
                    total += quantity * product.price
                if size == "medium":
                    total += quantity * (product.price + 12)
                if size == "large":
                    total += quantity * (product.price + 20)
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'total': total,
                })

    if (total > 0) and (total < settings.FREE_DELIVERY_THRESHOLD):
        delivery = settings.STANDARD_DELIVERY_PERCENTAGE #total * float(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        # if free_delivery_delta < 0:
        #     delivery = 0
        #     free_delivery_delta = 0
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    getcontext().prec = 4
    total = Decimal(total)
    grand_total = Decimal(grand_total)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
