from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart = request.session.get('cart', {})

    cart_items = []

    total = 0

    product_count = 0

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_id': item_id
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        # Case 1: Apply delivery charge, calculate both differences
        delivery_charge = 4.99
        free_delivery_difference = settings.FREE_DELIVERY_THRESHOLD - total
        free_tote_bag_difference = settings.FREE_TOTE_BAG_THRESHOLD - total

    elif settings.FREE_DELIVERY_THRESHOLD <= total < settings.FREE_TOTE_BAG_THRESHOLD:
        # Case 2: Free delivery but calculate tote bag difference
        delivery_charge = 0
        free_delivery_difference = 0
        free_tote_bag_difference = settings.FREE_TOTE_BAG_THRESHOLD - total

    else:
        # Case 3: Free delivery and tote bag achieved
        delivery_charge = 0
        free_delivery_difference = 0
        free_tote_bag_difference = 0


    grand_total = delivery_charge + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery_charge': delivery_charge,
        'free_delivery_difference': free_delivery_difference,
        'free_tote_bag_difference': free_tote_bag_difference,
        'free_tote_bag_threshold' : settings.FREE_TOTE_BAG_THRESHOLD,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context