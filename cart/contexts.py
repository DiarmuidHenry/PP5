from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


# def cart_contents(request):

#     cart = request.session.get('cart', {})

#     cart_items = []

#     subtotal = 0

#     product_count = 0

#     for unique_key, item_data in cart.items():
#         if isinstance(item_data, int):
#             product = get_object_or_404(Product, pk=item_id)
#             subtotal += item_data * product.price
#             product_count += item_data
#             cart_items.append({
#                 'item_id': item_id,
#                 'quantity': item_data,
#                 'product': product,
#             })
#         else:
#             product = get_object_or_404(Product, pk=item_id)
#             for size, quantity in item_data['items_by_size'].items():
#                 subtotal += quantity * product.price
#                 product_count += quantity
#                 cart_items.append({
#                     'item_id': item_id,
#                     'quantity': item_data,
#                     'product': product,
#                     'size': size,
#                 })

#     if subtotal < settings.FREE_DELIVERY_THRESHOLD:
#         # Case 1: Apply delivery charge, calculate both differences
#         delivery_charge = 4.99
#         free_delivery_difference = settings.FREE_DELIVERY_THRESHOLD - subtotal
#         free_tote_bag_difference = settings.FREE_TOTE_BAG_THRESHOLD - subtotal

#     elif settings.FREE_DELIVERY_THRESHOLD <= subtotal < settings.FREE_TOTE_BAG_THRESHOLD:
#         # Case 2: Free delivery but calculate tote bag difference
#         delivery_charge = 0
#         free_delivery_difference = 0
#         free_tote_bag_difference = settings.FREE_TOTE_BAG_THRESHOLD - subtotal

#     else:
#         # Case 3: Free delivery and tote bag achieved
#         delivery_charge = 0
#         free_delivery_difference = 0
#         free_tote_bag_difference = 0


#     total = delivery_charge + subtotal
    
#     context = {
#         'cart_items': cart_items,
#         'subtotal': subtotal,
#         'product_count': product_count,
#         'delivery_charge': delivery_charge,
#         'free_delivery_difference': free_delivery_difference,
#         'free_tote_bag_difference': free_tote_bag_difference,
#         'free_tote_bag_threshold' : settings.FREE_TOTE_BAG_THRESHOLD,
#         'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
#         'total': total,
#     }

#     return context

def cart_contents(request):

    cart = request.session.get('cart', {})
    cart_items = []
    subtotal = 0
    product_count = 0
    item_co2_footprint = Decimal("0.00")
    total_co2_footprint = Decimal("0.00")

    for unique_key, item_data in cart.items():
        print(f"Unique Key: {unique_key}, Item Data: {item_data}")

    print("type: unique_key")

    print(cart)



    for unique_key, item_data in cart.items():

        if isinstance(item_data, int):
            print("Item data is integer")
            product = get_object_or_404(Product, pk=unique_key)
            quantity = item_data
            item_total = product.price * quantity
            subtotal += item_total
            product_count += quantity
            item_co2_footprint = Decimal(product.co2_footprint * quantity).quantize(Decimal('0.01'))
            total_co2_footprint += item_co2_footprint  # Sum 
            cart_items.append({
                'product': product,
                'item_id': unique_key,
                'quantity': quantity,
                'item_total': item_total,
                'item_co2_footprint': item_co2_footprint,
            })
        else:
            product = get_object_or_404(Product, pk=item_data['product_id'])  # Retrieve product by ID
            quantity = item_data['quantity']
            item_id = item_data['product_id']
            selected_option = item_data.get('option')  # Get the selected option if it exists
            item_total = product.price * quantity
            subtotal += item_total
            product_count += quantity
            item_co2_footprint = Decimal(product.co2_footprint * quantity).quantize(Decimal('0.01'))
            total_co2_footprint += item_co2_footprint  # Sum 
            cart_items.append({
                'product': product,
                'item_id': item_id,
                'quantity': quantity,
                'option': selected_option,
                'item_total': item_total,
                'item_co2_footprint': item_co2_footprint,
            })
    
    if subtotal < settings.FREE_DELIVERY_THRESHOLD:
        # Case 1: Apply delivery charge, calculate both differences
        delivery_charge = settings.DELIVERY_CHARGE
        free_delivery_difference = settings.FREE_DELIVERY_THRESHOLD - subtotal
        free_tote_bag_difference = settings.FREE_TOTE_BAG_THRESHOLD - subtotal

    elif settings.FREE_DELIVERY_THRESHOLD <= subtotal < settings.FREE_TOTE_BAG_THRESHOLD:
        # Case 2: Free delivery but calculate tote bag difference
        delivery_charge = 0
        free_delivery_difference = 0
        free_tote_bag_difference = settings.FREE_TOTE_BAG_THRESHOLD - subtotal

    else:
        # Case 3: Free delivery and tote bag achieved
        delivery_charge = 0
        free_delivery_difference = 0
        free_tote_bag_difference = 0

    total = Decimal(delivery_charge) + subtotal
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'product_count': product_count,
        'delivery_charge': delivery_charge,
        'free_delivery_difference': free_delivery_difference,
        'free_tote_bag_difference': free_tote_bag_difference,
        'free_tote_bag_threshold' : settings.FREE_TOTE_BAG_THRESHOLD,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'total_co2_footprint': total_co2_footprint,
        'total': total,
    }

    return context