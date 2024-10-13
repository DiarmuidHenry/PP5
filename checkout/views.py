# from django.shortcuts import render, redirect, reverse
# from django.contrib import messages
# from .forms import OrderForm
# from .models import Order

# def checkout(request):
#     cart = request.session.get('cart', {})
#     if not cart:
#         messages.error(request, "There's nothing in your cart at the moment.")
#         return redirect(reverse('products'))

#     order_form = OrderForm()
#     template = 'checkout/checkout.html'
#     context = {
#         'order_form': order_form,
#         'cart': cart,
#     }

#     return render(request, template, context)

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from .models import Order
from products.models import Product  # Import the Product model

def checkout(request):

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment.")
        return redirect(reverse('products'))

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.order_items = cart  
            order.update_total() 
            order.save()  

            # Clear the cart from the session
            request.session['cart'] = {}
            messages.success(request, "Your order has been placed successfully!")
            return redirect(reverse('order_confirmation', args=[order.order_number]))
    else:
        order_form = OrderForm()

    product_count = sum(item['quantity'] for item in cart.values())

    # Fetch product details for each item in the cart
    products = {}
    for item in cart.values():
        product_id = item['product_id']
        try:
            product = Product.objects.get(id=product_id)
            products[product_id] = product
        except Product.DoesNotExist:
            products[product_id] = None
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        # 'cart': cart,
        # 'product_count': product_count,
        # 'products': products
        # 'total_order_cost': order.total_order_cost,
        # 'delivery_charge': order.delivery_charge,
        # 'total_co2_impact': order.total_co2_footprint,
    }

    print("Context data:")
    print(context)

    return render(request, template, context)

def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    context = {
        'order': order,
    }
    return render(request, 'checkout/order_confirmation.html', context)


# def checkout(request):
#     cart = request.session.get('cart', {})
#     if not cart:
#         messages.error(request, "There's nothing in your bag at the moment")
#         return redirect(reverse('products'))

#     order_form = OrderForm()
#     context = {
#         'order_form': order_form,
#     }

#     print("got to here")

#     return render(request, 'checkout/checkout.html', context)